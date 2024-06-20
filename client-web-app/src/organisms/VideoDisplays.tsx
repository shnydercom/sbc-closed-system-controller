import { Paper } from "@mui/material"

export const VideoDisplays = () => {
	return <Paper sx={{ padding: 2, display: "flex", flexDirection: "row", flexWrap: "wrap", gap: 5 }}>
		<img src="/video_feed_1"></img>
		<img src="/video_feed_1"></img>
	</Paper>
}