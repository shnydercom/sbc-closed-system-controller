import os
from enum import StrEnum
from time import sleep
import threading
from datetime import datetime, UTC
from utils import do_every
from hardwarecom.rpi_camera_streaming import StreamingCamera
from hardwarecom.sensorarray_streaming import StreamingSensorArray


class RECORDING_CONTENT(StrEnum):
    OUTER = "_outer_"
    INNER = "_inner_"
    SENSORS = "_sensors_"


def get_timestamp():
    return datetime.now(UTC).strftime("%Y-%m-%d_%H_%M_%S_%f")[:-3]


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
        sensor_array: StreamingSensorArray,
    ):
        self.recorder_start_datetime = None
        self.chunk_timeframe_size = chunk_timeframe_seconds
        self.inner_cam = inner_cam
        self.outer_cam = outer_cam
        self.sensor_array = sensor_array
        self.chunk_idx = 0
        self.is_recording = False
        # try to get to full seconds as closely as possible, with a bit of tolerance
        fullsec_wait = (999999 - datetime.now().microsecond - 100) / 999999
        sleep(fullsec_wait)
        self.timer_thread = threading.Thread(
            target=self.timer_thread_fn, name="datarecorder_timer_thread"
        )
        self.timer_thread.start()

    def timer_thread_fn(self):
        do_every(self.chunk_timeframe_size, self.trigger_filetransition)

    def make_filename(self, rec_content: RECORDING_CONTENT):
        filename = str(
            TODAYS_RECORDINGS
            + "/"
            + self.recorder_start_datetime
            + rec_content
            + str(self.chunk_idx)
        )
        return filename

    def trigger_start(self):
        if self.is_recording:
            raise ValueError("tried to start recording while system is recording")
        self.chunk_idx = 1
        self.recorder_start_datetime = get_timestamp()
        innercam_filename = self.make_filename(rec_content=RECORDING_CONTENT.INNER)
        outercam_filename = self.make_filename(rec_content=RECORDING_CONTENT.OUTER)
        sensors_filename = self.make_filename(rec_content=RECORDING_CONTENT.SENSORS)
        self.inner_cam.start_recording(innercam_filename)
        self.outer_cam.start_recording(outercam_filename)
        self.sensor_array.start_recording(sensors_filename)
        self.is_recording = True
        # do_every(20, self.trigger_filetransition)

    def trigger_filetransition(self):
        if not self.is_recording:
            return
        self.chunk_idx = self.chunk_idx + 1
        innercam_filename = self.make_filename(rec_content=RECORDING_CONTENT.INNER)
        outercam_filename = self.make_filename(rec_content=RECORDING_CONTENT.OUTER)
        sensors_filename = self.make_filename(rec_content=RECORDING_CONTENT.SENSORS)
        self.inner_cam.stop_recording()
        self.outer_cam.stop_recording()
        self.sensor_array.stop_recording()
        self.inner_cam.start_recording(innercam_filename)
        self.outer_cam.start_recording(outercam_filename)
        self.sensor_array.start_recording(sensors_filename)
        # print("transitioning file") # printing takes CPU time and leads to frame drops, only for debugging

    def trigger_stop(self):
        print("trigger stop")
        if not self.is_recording:
            raise ValueError("tried to stop recording while system is not recording")
        self.inner_cam.stop_recording()
        self.outer_cam.stop_recording()
        self.sensor_array.stop_recording()
        self.is_recording = False
        self.chunk_idx = 0
