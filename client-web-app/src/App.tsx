import { Paper } from '@mui/material';
import { PanTiltServoControls, LEDControls, SensorSummary, ExtraFanControl } from './organisms';


function App() {

	return (
		<>
			<Paper sx={{ marginLeft: 1, marginRight: 1, padding: 2 }}>
				<h1>Single Board Computer - Closed System Controller</h1>
				<PanTiltServoControls />
				<SensorSummary />
				<LEDControls />
				<ExtraFanControl />
			</Paper>
		</>
	)
}

export default App
