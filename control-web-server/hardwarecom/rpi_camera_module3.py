#!/usr/bin/python3
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
