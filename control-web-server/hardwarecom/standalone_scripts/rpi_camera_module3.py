#!/usr/bin/python3
# example code repo: https://github.com/raspberrypi/picamera2/tree/main/examples
from threading import Condition

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput

lsize = (320, 240)
picam2 = Picamera2()
video_config = picam2.create_video_configuration(
    main={"size": (1280, 720), "format": "RGB888"},
    lores={"size": lsize, "format": "YUV420"},
)

picam2.configure(video_config)
encoder1 = H264Encoder(1000000, repeat=True)


# encoder = JpegEncoder(q=70)
# picam2.start_recording(encoder, "test.mjpeg", pts="timestamp.txt")

# import libcamera
# preview_config = picam2.create_preview_configuration()
# preview_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
# picam2.configure(preview_config)

# Obtain the current camera control values in the image metadata.
# preview_config = picam2.create_preview_configuration()
# picam2.capture_metadata()
encoder = H264Encoder(10000000)
picam2.start_recording(encoder, "test.h264", pts="timestamp.txt")
"""
picam2 = Picamera2()
video_config = picam2.create_video_configuration(
    use_case="video",
    display=None,
    controls={"FrameDurationLimits": [33333, 33333]},
    # colour_space="sYCC",
    # encode="main",
    main={"size": (1920, 1080)},
    lores={"size": (320, 240)},
    encode="lores",
)
picam2.configure(video_config)


picam2.encoders

class FileOutputStop(FileOutput):
    def __init__(self, file=None, pts=None, split=None):
        super().__init__(file, pts, split)
        self.frame_counter = 0
        self.cond = Condition()

    def _write(self, frame, timestamp=None):
        self.frame_counter += 1
        # Stop capturing when 200 frames is reached
        if self.frame_counter <= 200:
            super()._write(frame, timestamp)
            if self.frame_counter == 200:
                with self.cond:
                    self.stop()
                    self.cond.notify()


encoder = H264Encoder(10000000, framerate=30)
encoder.output = FileOutputStop("test.h264")
picam2.start_encoder(encoder)
picam2.start()

# Wait for 200 frames to be captured
with encoder.output.cond:
    encoder.output.cond.wait()
"""
