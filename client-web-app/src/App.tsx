import { AppBar, Paper, Stack, Toolbar } from '@mui/material';
import { PanTiltServoControls, LEDControls, SensorSummary, ExtraFanControl, VideoDisplays, RecorderFlow } from './organisms';

/*
<h1>Single Board Computer - Closed System Controller</h1>
*/

function App() {
	return (
		<>
			<AppBar position="static">
				<Toolbar variant="dense">
					<RecorderFlow />
				</Toolbar>
			</AppBar>
			<Paper sx={{ marginLeft: 1, marginRight: 1, padding: 2 }}>
				<Stack direction="row" gap={2} flexWrap={'wrap'}>
					<Stack direction="column" gap={1}>
						<PanTiltServoControls />
						<VideoDisplays />
						<LEDControls />
						<ExtraFanControl />
					</Stack>
					<Stack direction="column">
						<SensorSummary />
					</Stack>
				</Stack>
			</Paper>
		</>
	)
}

export default App
