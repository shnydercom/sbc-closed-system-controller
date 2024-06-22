import io
from threading import Condition
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

from picamera2 import Picamera2


class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()


class StreamingCamera:
    def __init__(self, camera_num):
        self.picam2 = Picamera2(camera_num)
        self.picam2.configure(
            self.picam2.create_video_configuration(main={"size": (640, 480)})
        )
        self.output = StreamingOutput()
        self.picam2.start_recording(JpegEncoder(), FileOutput(self.output))

    def get_frame(self):
        try:
            while True:
                with self.output.condition:
                    self.output.condition.wait()
                    frame = self.output.frame

                ret = b"--FRAME\r\n"
                ret += b"Content-Type: image/jpeg\r\n"
                ret += f"Content-Length: {len(frame)}\r\n\r\n".encode()
                ret += frame
                ret += b"\r\n"
                yield ret
        except Exception as e:
            print("Removed streaming client!" + e)
