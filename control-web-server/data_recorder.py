from datetime import datetime, UTC
from hardwarecom.rpi_camera_streaming import StreamingCamera
import os


def get_timestamp():
    return datetime.now(UTC).strftime("%Y-%m-%d_%H:%M:%S.%f")[:-3]


serverstart_date = datetime.now(UTC).strftime("%Y-%m-%d")

FOLDER_RECORDINGS = "./../recordings/"
TODAYS_RECORDINGS = FOLDER_RECORDINGS + serverstart_date

if not os.path.exists(FOLDER_RECORDINGS):
    os.mkdir(FOLDER_RECORDINGS)

if not os.path.exists(TODAYS_RECORDINGS):
    os.mkdir(TODAYS_RECORDINGS)


class DataRecorder:
    def __init__(
        self,
        chunk_timeframe_seconds,
        inner_cam: StreamingCamera,
        outer_cam: StreamingCamera,
    ):
        self.recorder_start_datetime = None
        self.chunk_timeframe_size = chunk_timeframe_seconds
        self.inner_cam = inner_cam
        self.outer_cam = outer_cam
        self.chunk_idx = 0
        self.is_recording = False

    def trigger_start(self):
        self.recorder_start_datetime = get_timestamp()
        innercam_filename = str(
            TODAYS_RECORDINGS
            + "/"
            + self.recorder_start_datetime
            + "_innerCam_"
            + str(self.chunk_idx)
        )
        outercam_filename = str(
            TODAYS_RECORDINGS
            + "/"
            + self.recorder_start_datetime
            + "_outerCam_"
            + str(self.chunk_idx)
        )
        self.inner_cam.start_recording(innercam_filename)
        self.outer_cam.start_recording(outercam_filename)
        self.is_recording = True

    def trigger_stop(self):
        self.inner_cam.stop_recording()
        self.outer_cam.stop_recording()
        self.is_recording = False
