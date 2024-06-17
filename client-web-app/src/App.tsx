import { useState } from 'react'
import { Button } from '@mui/material'
import { PanTiltButtons, PanTiltButtonsProps } from "./components";

function App() {
	const [panTiltText, setPanTiltText] = useState("pantilt text")

	const pantiltProps: PanTiltButtonsProps = {
		isRelative: false,
		panRange: [-60, 60],
		panStepsCount: 5,
		tiltRange: [-60, 60],
		tiltStepsCount: 5,
		onDirectionButtonClicked: ({pan, tilt}) => {
			setPanTiltText(`pan is ${pan}, tilt is ${tilt}`)
		},
		gridContainerStyles: {
			width: "500px",
			height: "400px"
		}
	}
	return (
		<>
			<h1>Single Board Computer - Closed System Controller</h1>
			<div className="card">
				<Button onClick={() => setPanTiltText((count) => count + 1)}>
					text: {panTiltText}
				</Button>
				<PanTiltButtons {...pantiltProps}/>
			</div>
		</>
	)
}

export default App
