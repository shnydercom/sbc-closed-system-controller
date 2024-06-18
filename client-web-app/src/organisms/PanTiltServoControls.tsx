import { useEffect, useState } from 'react'
import { Box, Typography } from '@mui/material'
import { PanTiltButtons, PanTiltButtonsProps } from "../molecules";
import { DefaultApi } from "./../api/axios-client";
import { PanTiltCombo } from './../interfaces';

import { useAppDispatch, useTypedSelector } from '../store/reduxStore'

const api = new DefaultApi(undefined, ".")

export function PanTiltServoControls() {
	const [lastPanTilt, setLastPanTilt] = useState<PanTiltCombo>({ pan: Infinity, tilt: Infinity })

	const dispatch = useAppDispatch()
	
	useEffect(() => {
		api.pantiltOrientation().then((res) => {
			setLastPanTilt({ ...lastPanTilt, ...res.data })
		})
	}, [])
	const pantiltProps: PanTiltButtonsProps = {
		panRange: [-20, 20],
		panStepsCount: 5,
		tiltRange: [-20, 20],
		tiltStepsCount: 5,
		onDirectionButtonClicked: ({ pan, tilt }) => {
			if (pan === 0 && tilt === 0) {
				Promise.all([
					api.panToMiddle(),
					api.tiltToMiddle()]
				).then(([resPan, resTilt]) => {
					setLastPanTilt(({ pan: resPan.data.pan ?? Infinity, tilt: resTilt.data.tilt ?? Infinity }))
				})
				return;
			}
			Promise.all([
				api.panBy({ relativeangle: pan }),
				api.tiltBy({ relativeangle: tilt })]
			).then(([resPan, resTilt]) => {
				setLastPanTilt(({ pan: resPan.data.pan ?? Infinity, tilt: resTilt.data.tilt ?? Infinity }))
			})
		},
		gridContainerStyles: {
			width: "500px",
			height: "400px"
		}
	}
	return (
		<>
			<Box mb={2}>
				<Typography>Pan: {lastPanTilt.pan}</Typography>
				<Typography>Tilt: {lastPanTilt.tilt}</Typography>
			</Box>
			<PanTiltButtons {...pantiltProps} />
		</>
	);
}