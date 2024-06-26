import { Box, Button, SxProps, Theme } from '@mui/material';
import { useMemo } from 'react';

export interface PanTiltButtonsProps {
	panRange: [number, number];
	tiltRange: [number, number];
	panStepsCount: number;
	tiltStepsCount: number;
	onDirectionButtonClicked: (newPanTilt: { pan: number, tilt: number }) => void;
	unit?: string;
	gridContainerStyles?: SxProps<Theme>
}

export const PanTiltButtons: React.FC<PanTiltButtonsProps> = ({ panRange, tiltRange, panStepsCount, tiltStepsCount, onDirectionButtonClicked, unit, gridContainerStyles }: PanTiltButtonsProps) => {

	const directionButtons = useMemo(() => {
		const unitStr = unit ?? "°";
		const result: React.ReactElement[] = [];
		const panMin = Math.min(...panRange);
		const panMax = Math.max(...panRange);
		const panDeltaSteps = (panMax - panMin) / (panStepsCount - 1);
		const tiltMin = Math.min(...tiltRange);
		const tiltMax = Math.max(...tiltRange);
		const tiltDeltaSteps = (tiltMax - tiltMin) / (tiltStepsCount - 1);
		//for (let tiltIterator = tiltStepsCount - 1; tiltIterator >= 0; tiltIterator--) {
		for (let tiltIterator = 0; tiltIterator < tiltStepsCount; tiltIterator++) {
			for (let panIterator = panStepsCount - 1; panIterator >= 0; panIterator--) {
				const newPan = panIterator * panDeltaSteps + panMin;
				const newTilt = tiltIterator * tiltDeltaSteps + tiltMin;
				const btnText: string = `← ${newPan}${unitStr} ↓${newTilt}${unitStr}`;
				const newButton = <Button
					key={`ptBtn-${tiltIterator}-${panIterator}`}
					size='small'
					sx={{fontSize: "0.75rem"}}
					onClick={() => {
						onDirectionButtonClicked({ pan: newPan, tilt: newTilt })
					}}
					variant="contained">{btnText}</Button>
				result.push(newButton);
			}
		}
		return result;
	}, [panRange, tiltRange, panStepsCount, tiltStepsCount])

	return (
		<Box sx={{
			display: "grid",
			gridTemplateColumns: `repeat(${panStepsCount}, 1fr)`,
			gridTemplateRows: `repeat(${tiltStepsCount}, 1fr)`,
			gridColumnGap: "3px",
			gridRowGap: "3px",
			...(gridContainerStyles ?? {})
		}}>
			{directionButtons}
		</Box>
	);
};