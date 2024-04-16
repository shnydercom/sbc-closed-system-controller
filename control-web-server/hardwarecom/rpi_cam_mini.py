#!/usr/bin/python3
# from picamera2 import Picamera2

# picam2 = Picamera2()
# picam2.start_and_record_video("test2.h264", duration=5)
import time
from picamera2 import Picamera2

from picamera2.encoders import H264Encoder

from picamera2.outputs import FileOutput
import logging

cam = Picamera2()

video_config = cam.create_video_configuration(
    main={"size": (1640, 1232), "format": "YUV420"},
    lores={"size": (640, 480), "format": "YUV420"},
)

highres_encoder = H264Encoder(
    10_000_000,
    iperiod=120,
    framerate=25,  # enable_sps_framerate=True
)
highres_output = FileOutput("highres.mp4")

lowres_encoder = H264Encoder(
    700_000,
    iperiod=120,
    framerate=25,  # enable_sps_framerate=True
)
lowres_output = FileOutput("lowres.mp4")

cam.configure(video_config)
cam.set_controls({"FrameRate": 25})
cam.start()
cam.start_encoder(highres_encoder, highres_output)  # Start highres recording
cam.start_encoder(lowres_encoder, lowres_output, name="lores")  # Start lowres recording

time.sleep(5)

cam.stop_encoder(encoders=lowres_encoder)  # Stop only lowres recording

cam.stop_recording()  # Stop all recordings
cam.stop()
