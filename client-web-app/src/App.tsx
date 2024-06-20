import { Paper } from '@mui/material';
import { PanTiltServoControls } from './organisms';
import { SensorSummary } from './organisms';
import { LEDControls } from './organisms/LEDControls';


function App() {

	return (
		<>
			<Paper sx={{marginLeft: 1, marginRight: 1, padding:2}}>
			<h1>Single Board Computer - Closed System Controller</h1>
				<PanTiltServoControls/>
				<SensorSummary/>
				<LEDControls/>
			</Paper>
		</>
	)
}

export default App
