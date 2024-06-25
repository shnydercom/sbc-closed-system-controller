import { AppBar, Paper, Stack, Toolbar } from '@mui/material';
import { PanTiltServoControls, LEDControls, SensorSummary, ExtraFanControl, VideoDisplays, RecorderFlow } from './organisms';
import useMediaQuery from '@mui/material/useMediaQuery';

/*
<h1>Single Board Computer - Closed System Controller</h1>
*/

function App() {
	const matches = useMediaQuery('(min-width:600px)');
	const PaperOrNoPaper = matches
		? (props: React.PropsWithChildren<{}>) =>
			<Paper sx={{ margin: 1 }}>{props.children}</Paper>
		: (props: React.PropsWithChildren<{}>) => <>{props.children}</>
	return (
		<>
			<AppBar position="static">
				<Toolbar variant="dense">
					<RecorderFlow />
				</Toolbar>
			</AppBar>
			<PaperOrNoPaper>
				<Stack direction="row" gap={2} flexWrap={'wrap'} padding={2}>
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
			</PaperOrNoPaper>
		</>
	)
}

export default App
