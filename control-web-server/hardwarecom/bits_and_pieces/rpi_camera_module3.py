#!/usr/bin/python3
# code link: https://github.com/raspberrypi/picamera2/blob/main/examples/mjpeg_server_with_rotation.py

# This is the same as mjpeg_server_2.py, but allows 90 or 270 degree rotations.

import io
from threading import Condition, Thread
from _thread import get_ident

import piexif

from picamera2 import Picamera2
from picamera2.encoders import MJPEGEncoder
from picamera2.outputs import FileOutput

ROTATION = 0  # Use 0, 90 or 270
WIDTH = 640
HEIGHT = 480

rotation_header = bytes()
if ROTATION:
    WIDTH, HEIGHT = HEIGHT, WIDTH
    code = 6 if ROTATION == 90 else 8
    exif_bytes = piexif.dump({"0th": {piexif.ImageIFD.Orientation: code}})
    exif_len = len(exif_bytes) + 2
    rotation_header = bytes.fromhex("ffe1") + exif_len.to_bytes(2, "big") + exif_bytes


class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf[:2] + rotation_header + buf[2:]
            self.condition.notify_all()


class StreamRecorderCamera:
    def __init__(self, camera_num):
        self._thread = Thread(target=self._thread_func, daemon=True)
        self.camera_num = camera_num
        self.picam2 = Picamera2(camera_num)
        self.picam2.configure(
            self.picam2.create_video_configuration(main={"size": (640, 480)})
        )
        self.outputStream = None
        self.frame = None

    def _frame_func(self):
        self.outputStream = StreamingOutput()
        self.picam2.start_recording(MJPEGEncoder(), FileOutput(self.outputStream))
        try:
            with self.outputStream.condition:
                self.outputStream.condition.wait()
                frame = self.outputStream.frame
            yield frame
        except Exception as e:
            print(str(e))

    def _thread_func(self):
        frames_iterator = None
        try:
            frames_iterator = self._frame_func()
            print(
                "Thread %s: Camera._thread2 - frames_iterator instantiated", get_ident()
            )
            for frame in frames_iterator:
                self.frame = frame
        except Exception as e:
            print("Thread %s: Camera._thread2 - Exception: %s", get_ident(), e)

    def start(self):
        if not self._thread.is_alive():
            self._thread.start()

    def get_latest_output(self):
        self.frame

    def stop_recording(self):
        self.picam2.stop_recording()
