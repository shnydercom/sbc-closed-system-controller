import { FormControlLabel, Stack, Switch, Typography } from "@mui/material";
import { useCoolerStrengthQuery, useLazySwitchCoolerOffQuery, useLazySwitchCoolerOnQuery } from "../store/rtkQueryClientApi"

export const ExtraFanControl = () => {
	const coolerStrengthQ = useCoolerStrengthQuery(undefined, { pollingInterval: 500 })
	const [triggerCoolerOff, _coolerOffQ] = useLazySwitchCoolerOffQuery()
	const [triggerCoolerOn, _coolerOnQ] = useLazySwitchCoolerOnQuery();
	const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		if (event.target.checked) {
			triggerCoolerOn()
			return
		}
		triggerCoolerOff()
	};
	const booleanCoolerValue = (coolerStrengthQ.data?.strength ?? 0) > 0
	return (
		<Stack direction="column" mt={2}>
			<Typography variant="caption">Extra Fan Control</Typography>
			<FormControlLabel control={
				<Switch
					checked={booleanCoolerValue}
					onChange={handleChange}
					disabled={!coolerStrengthQ.isSuccess || _coolerOffQ.isLoading || _coolerOnQ.isLoading}
				/>
			} label="0 or 100% fan speed" />
		</Stack>
	);
}