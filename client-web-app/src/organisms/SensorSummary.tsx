import { Box } from "@mui/material";
import { MomentSensorReadings, MomentSensorReadingsProps } from "../molecules";

import { useCurrentSensorQuery, useAccelerometerGyroSensorQuery } from "../store/rtkQueryClientApi"

export const SensorSummary = () => {
	const sensorReadings: MomentSensorReadingsProps[] = [];
	const currentSensorQ = useCurrentSensorQuery();
	const accelerometerQ = useAccelerometerGyroSensorQuery();

	if (currentSensorQ.isSuccess) {
		const currentSensorFormatted = formatValuesToString(currentSensorQ.data);
		sensorReadings.push({ sensorHeading: "power-sensor (in V, mA, W)", readings: currentSensorFormatted })
	}
	if (accelerometerQ.isSuccess) {
		const accelGyroSensorFormatted = formatValuesToString(accelerometerQ.data);
		sensorReadings.push({ sensorHeading: "accelerometer (in m/s^2, radians/s)", readings: accelGyroSensorFormatted })
	}
	return (
		<Box>
			{
				sensorReadings.map((sensorReading, idx) => {
					return <MomentSensorReadings
						key={`sensor-${idx}`}
						sensorHeading={sensorReading.sensorHeading}
						readings={sensorReading.readings}
					/>
				})
			}
		</Box>
	);
}

const valFormatter = (val: any): string => {
	if (typeof val === 'number') {
		return val.toFixed(3);
	}
	if (Array.isArray(val)) {
		return val.map((valEntry) => valFormatter(valEntry)).join("; ")
	}
	return "" + val
}

const formatValuesToString = (inputObj: { [s: string]: any }): {
	[s: string]: string;
} => {
	const result = Object.fromEntries(
		Object.entries(inputObj).map(([key, val]) => {
			return [key, valFormatter(val)]
		}),
	);
	return result
}