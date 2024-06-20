import { Paper } from "@mui/material"

export const VideoDisplays = () => {
	return <Paper sx={{ padding: 2, display: "flex", flexDirection: "row", flexWrap: "wrap", gap: 5 }}>
		<img src="/rest/outer-video-stream"></img>
		<img src="/rest/inner-video-stream"></img>
	</Paper>
}