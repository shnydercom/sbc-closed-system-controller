import { Paper, Stack } from '@mui/material';
import { PanTiltServoControls, LEDControls, SensorSummary, ExtraFanControl, VideoDisplays } from './organisms';


function App() {

	return (
		<>
			<Paper sx={{ marginLeft: 1, marginRight: 1, padding: 2 }}>
				<h1>Single Board Computer - Closed System Controller</h1>
				<Stack direction="row" gap={2} flexWrap={'wrap'}>
					<Stack direction="column" gap={1}>
						<PanTiltServoControls />
						<LEDControls />
						<ExtraFanControl />
					</Stack>
					<Stack direction="column">
						<VideoDisplays/>
						<SensorSummary />
					</Stack>
				</Stack>
			</Paper>
		</>
	)
}

export default App
