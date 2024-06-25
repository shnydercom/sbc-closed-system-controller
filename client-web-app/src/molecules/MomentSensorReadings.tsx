import { Box, Typography } from "@mui/material";

export interface MomentSensorReadingsProps {
	sensorHeading: string;
	readings: { [s: string]: string }
	isWarning?: boolean;
}
export const MomentSensorReadings = ({ sensorHeading, readings, isWarning }: MomentSensorReadingsProps) => {
	const descriptions = Array.from(Object.keys(readings));
	return (
		<Box display={"flex"} flexDirection={"column"} mt={2}>
			<Typography variant="caption">{sensorHeading}</Typography>
			<Box 
				display={"grid"} 
				gridAutoFlow="column" 
				gap="4px" 
				gridTemplateRows={`repeat(${descriptions.length}, 24px)`} gridTemplateColumns={"120px"}
				bgcolor={isWarning ? "red" : undefined}
				>
				{descriptions.map((entry, idx) => {
					return (
						<Typography key={`desc-${idx}`}>{entry}</Typography>
					)
				}
				)}
				<VolatileSensorReadingText readings={Object.values(readings)} />
			</Box>
		</Box>
	);
}

const VolatileSensorReadingText = ({ readings }: { readings: string[] }) => {
	//might update UI here, where all quick changes happen
	return (<>
		{readings.map((reading, idx) => <Typography key={`reading-${idx}`}>{reading}</Typography>)}
	</>)
}