import { Stack, Typography, debounce } from "@mui/material";
import { PercentageControlRow } from "../molecules";
import { PercentageControl } from "../interfaces";
import { useGetAllLedStrengthsQuery, useLazySwitchLedToQuery } from "../store/rtkQueryClientApi"

export const LEDControls = () => {
	const ledStrengths = useGetAllLedStrengthsQuery(undefined, { pollingInterval: 500 });
	const [triggerLEDSwitch, changedLedStrength] = useLazySwitchLedToQuery();
	let upperLeds: PercentageControl[] = [];
	let lowerLeds: PercentageControl[] = [];
	if (ledStrengths.isSuccess) {
		upperLeds = ledStrengths.data.map((pwmDevice) => {
			const result: PercentageControl = { identifier: pwmDevice.identifier ?? -1, percentage: pwmDevice.strength ?? -1 }
			return result;
		})
		if (changedLedStrength.isSuccess) {
			const led = upperLeds.find((pcCtrl) => pcCtrl.identifier === changedLedStrength.data.identifier)
			if (led) {
				led.percentage = changedLedStrength.data.strength ?? -1;
			}
		}
		lowerLeds = upperLeds.splice(Math.floor(upperLeds.length / 2), Math.floor(upperLeds.length / 2))
		//reversing because of physical orientation of camera to LED rows
		upperLeds.reverse()
		lowerLeds.reverse()
	}

	const onChange = debounce((nextValue: PercentageControl) => {
		triggerLEDSwitch({ ledId: nextValue.identifier, nextStrength: nextValue.percentage })
	}, 200)

	return (
		<Stack direction={"column"} mt={2}>
			<Typography variant="caption">Upper LEDs</Typography>
			<PercentageControlRow controls={upperLeds} onChange={onChange} />
			<Typography variant="caption" mt={2}>Lower LEDs</Typography>
			<PercentageControlRow controls={lowerLeds} onChange={onChange} />
		</Stack>);
}