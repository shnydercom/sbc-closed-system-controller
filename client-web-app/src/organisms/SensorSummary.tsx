import { Box } from "@mui/material";
import { DefaultApi } from "../api/axios-client";
import { MomentSensorReadings, MomentSensorReadingsProps } from "../molecules";
import { useEffect, useState } from "react";

const api = new DefaultApi(undefined, ".")

export const SensorSummary = () => {
	const [sensorReadings, setSensorReadings] = useState<MomentSensorReadingsProps[]>([])
	useEffect(() => {
		Promise.all(
			[
				api.currentSensor(),
				api.accelerometerGyroSensor()
			]
		).then(([currentSensorRes, accelRes]) => {
			const currentSensorFormatted = formatValuesToString(currentSensorRes.data);
			const accelGyroSensorFormatted = formatValuesToString(accelRes.data);
			setSensorReadings([
				{ sensorHeading: "power-sensor (in V, mA, W)", readings: currentSensorFormatted },
				{ sensorHeading: "accelerometer (in m/s^2, radians/s)", readings: accelGyroSensorFormatted }
			])
		})
	}, [])
	return (
		<Box>
			{
				sensorReadings.map((sensorReading) => {
					return <MomentSensorReadings sensorHeading={sensorReading.sensorHeading} readings={sensorReading.readings} />
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