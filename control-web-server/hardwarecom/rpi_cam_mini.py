from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_record_video("test2.h264", duration=5)
