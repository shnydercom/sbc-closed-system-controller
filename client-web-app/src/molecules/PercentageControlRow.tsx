import { Stack, Slider, SliderProps } from "@mui/material";
import { FunctionComponent } from "react";
import { PercentageControl } from "../interfaces";

interface PercentageControlRowProps {
	controls: PercentageControl[];
	onChange: (nextValue: PercentageControl) => void
}

function valuetext(value: number) {
	return `${value * 100} %`;
}

export const PercentageControlRow: FunctionComponent<PercentageControlRowProps> = ({ controls, onChange }) => {
	const createOnSliderChange = (id: number): SliderProps["onChange"] => (_e, val) => {
		if (Array.isArray(val)) {
			throw new Error("expected slider to have single value");
		}
		onChange({ identifier: id, percentage: val })
	}
	return (
		<Stack sx={{ height: 150 }} spacing={1} direction="row">
			{controls.map((control, idx) => {
				const onSliderChange = createOnSliderChange(control.identifier);
				return (<Slider
					key={`slider-${idx}`}
					value={control.percentage}
					min={0.0}
					step={0.2}
					max={1.0}
					onChange={onSliderChange}
					orientation="vertical"
					size="small"
					getAriaValueText={valuetext}
					valueLabelDisplay="auto"
					defaultValue={0.0}
				/>)
			})}
		</Stack>);
}