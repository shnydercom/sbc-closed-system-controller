import { ToggleButton } from "@mui/material"
import FiberManualRecordIcon from '@mui/icons-material/FiberManualRecord';
import StopIcon from '@mui/icons-material/Stop';
import QuestionMarkIcon from '@mui/icons-material/QuestionMark';
import { useIsDataRecordingQuery, useLazyStartRecorderQuery, useLazyStopRecorderQuery } from "../store/rtkQueryClientApi";

export const RecorderFlow = () => {
	const isRecordingQ = useIsDataRecordingQuery(undefined, { pollingInterval: 300 })
	const [triggerRecordingStart, _recordingStartQ] = useLazyStartRecorderQuery()
	const [triggerRecordingStop, _recordingStopQ] = useLazyStopRecorderQuery();
	const handleChange = () => {
		if (!isRecordingValue) {
			triggerRecordingStart()
			return
		}
		triggerRecordingStop()
	};
	const isRecordingValue = isRecordingQ.data ?? false;
	return <>
		<ToggleButton sx={{ mr: 2 }}
			disabled={!isRecordingQ.isSuccess || _recordingStartQ.isLoading || _recordingStopQ.isLoading}
			value="check"
			selected={isRecordingValue}
			onChange={handleChange}>
			{
				isRecordingQ.data === undefined
					? <QuestionMarkIcon />
					: isRecordingQ.data
						? <StopIcon />
						: <FiberManualRecordIcon />
			}
		</ToggleButton>
	</>
}