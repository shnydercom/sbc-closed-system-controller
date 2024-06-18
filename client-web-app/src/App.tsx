import { PanTiltServoControls } from './organisms';
import { SensorSummary } from './organisms';


function App() {

	return (
		<>
			<h1>Single Board Computer - Closed System Controller</h1>
			<div className="card">
				<PanTiltServoControls/>
				<SensorSummary/>
			</div>
		</>
	)
}

export default App
