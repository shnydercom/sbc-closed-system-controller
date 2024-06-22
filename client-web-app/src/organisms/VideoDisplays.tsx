import { Paper } from "@mui/material"

export const VideoDisplays = () => {
	return <Paper sx={{ padding: 0, display: "flex", flexDirection: "row", flexWrap: "wrap", gap: "2px" }}>
		<img src="/rest/outer-video-stream" width="320px" height="240px"></img>
		<img src="/rest/inner-video-stream" width="320px" height="240px"></img>
	</Paper>
}