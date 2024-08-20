import { Box } from "@mui/material";
import { MomentSensorReadings, MomentSensorReadingsProps } from "../molecules";

import { useCurrentSensorQuery, useAccelerometerGyroSensorQuery, useSystemHealthSensorsQuery, useSolarChargerQuery } from "../store/rtkQueryClientApi"

export const SensorSummary = () => {
	const sensorReadings: MomentSensorReadingsProps[] = [];
	const currentSensorQ = useCurrentSensorQuery(undefined, { pollingInterval: 500 });
	const accelerometerQ = useAccelerometerGyroSensorQuery(undefined, { pollingInterval: 2000 });
	const systemHealthQ = useSystemHealthSensorsQuery(undefined, {pollingInterval: 2000})
	const solarChargerQ = useSolarChargerQuery(undefined, {pollingInterval: 2000});

	if (currentSensorQ.isSuccess) {
		const currentSensorFormatted = formatValuesToString(currentSensorQ.data);
		sensorReadings.push({ sensorHeading: "power-sensor (in V, mA, W)", readings: currentSensorFormatted })
	}
	if (accelerometerQ.isSuccess) {
		const accelGyroSensorFormatted = formatValuesToString(accelerometerQ.data);
		sensorReadings.push({ sensorHeading: "accelerometer (in m/s^2, radians/s)", readings: accelGyroSensorFormatted })
	}
	if ( systemHealthQ.isSuccess) {
		const systemHealthFormatted = formatValuesToString(systemHealthQ.data);
		const isWarning = systemHealthQ.data.cpu_temp > 48;
		sensorReadings.push({ sensorHeading: "system health (CPU temp, usage)", readings: systemHealthFormatted, isWarning})
	}
	if ( solarChargerQ.isSuccess) {
		const solarChargingFormatted = formatValuesToString(solarChargerQ.data);
		sensorReadings.push({ sensorHeading: "solar charger (Status LEDs)", readings: solarChargingFormatted})
	}

	return (
		<Box>
			{
				sensorReadings.map((sensorReading, idx) => {
					return <MomentSensorReadings
						key={`sensor-${idx}`}
						sensorHeading={sensorReading.sensorHeading}
						readings={sensorReading.readings}
						isWarning={sensorReading.isWarning}
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