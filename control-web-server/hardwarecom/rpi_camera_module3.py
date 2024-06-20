#!/usr/bin/python3
# code link: https://github.com/raspberrypi/picamera2/blob/main/examples/mjpeg_server_with_rotation.py

# This is the same as mjpeg_server_2.py, but allows 90 or 270 degree rotations.

import io
import logging
import socketserver
from http import server
from threading import Condition

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
        self.camera_num = camera_num
        self.picam2 = Picamera2(camera_num)
        self.picam2.configure(
            self.picam2.create_video_configuration(main={"size": (640, 480)})
        )
        self.outputStream = StreamingOutput()
        self.picam2.start_recording(MJPEGEncoder(), FileOutput(self.outputStream))

    def get_latest_output(self):
        try:
            with self.outputStream.condition:
                self.outputStream.condition.wait()
                frame = self.outputStream.frame
            return frame
        except Exception as e:
            logging.warning(str(e))

    def stop_recording(self):
        self.picam2.stop_recording()
