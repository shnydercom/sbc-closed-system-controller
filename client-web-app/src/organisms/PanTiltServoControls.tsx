import { Box, Typography } from '@mui/material'
import { PanTiltButtons, PanTiltButtonsProps } from "../molecules";
import { PanTiltCombo } from './../interfaces';

import { usePantiltOrientationQuery, useLazyPanToMiddleQuery, useLazyTiltToMiddleQuery, useLazyPanByQuery, useLazyTiltByQuery } from "../store/rtkQueryClientApi"

export function PanTiltServoControls() {
	let lastPanTilt: PanTiltCombo = { pan: Infinity, tilt: Infinity }

	const orientationQuery = usePantiltOrientationQuery()

	const [triggerPanMid, panMidQueryResult] = useLazyPanToMiddleQuery();
	const [triggerTiltMid, tiltMidQueryResult] = useLazyTiltToMiddleQuery();
	const [triggerPanBy, panByQueryResult] = useLazyPanByQuery()
	const [triggerTiltBy, tiltByQueryResult] = useLazyTiltByQuery()

	let allQueries = [orientationQuery, panMidQueryResult, tiltMidQueryResult, panByQueryResult, tiltByQueryResult]

	allQueries = allQueries.filter((query) => query.isSuccess).sort((a,b) => ((b.fulfilledTimeStamp ?? 1)-(a.fulfilledTimeStamp ?? 1)))
	if(allQueries.length > 0) {
		lastPanTilt = { ...lastPanTilt, ...allQueries[0].data }
	}

	if (orientationQuery.isError) {
		return (
			<div>
				<h1>There was an error!!!</h1>
			</div>
		)
	}
	if (orientationQuery.isLoading) {
		return (
			<div>
				<h1>Loading...</h1>
			</div>
		)
	}

	if (orientationQuery.isSuccess) {
		const pantiltProps: PanTiltButtonsProps = {
			panRange: [-20, 20],
			panStepsCount: 5,
			tiltRange: [-20, 20],
			tiltStepsCount: 5,
			onDirectionButtonClicked: ({ pan, tilt }) => {
				if (pan === 0 && tilt === 0) {
					triggerPanMid()
					triggerTiltMid()
					return;
				}
				triggerPanBy({ relativeangle: pan })
				triggerTiltBy({ relativeangle: tilt })
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
	return null;
}