import io
from threading import Condition
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder, H264Encoder
from picamera2.outputs import FileOutput, FfmpegOutput

from datetime import datetime, UTC
import cv2

from picamera2 import Picamera2, MappedArray


class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()


# timestamp on the recordings in the top right corner
colour = (255, 255, 255)
origin = (0, 8)
font = cv2.FONT_HERSHEY_PLAIN
scale = 0.5
thickness = 1


class StreamingCamera:
    def __init__(self, camera_idx):
        self.picam2 = Picamera2(camera_idx)
        self.picam2.configure(
            self.picam2.create_video_configuration(
                main={"size": (1920, 1080)},
                lores={"size": (320, 240), "format": "RGB888"},
            )
        )
        self.web_streaming_output = StreamingOutput()
        self.recording_encoder = H264Encoder(10000000, framerate=30)
        self.picam2.pre_callback = self._apply_timestamp
        self.picam2.start_recording(
            JpegEncoder(), FileOutput(self.web_streaming_output), name="lores"
        )

    def _apply_timestamp(self, request):
        timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        with MappedArray(request, "main") as m:
            cv2.putText(m.array, timestamp, origin, font, scale, colour, thickness)

    def start_recording(self, output_filename):
        output = FfmpegOutput(output_filename + ".mp4")
        self.picam2.start_encoder(self.recording_encoder, output, name="main")

    def stop_recording(self):
        self.picam2.stop_encoder(self.recording_encoder)

    def get_frame(self):
        try:
            while True:
                with self.web_streaming_output.condition:
                    self.web_streaming_output.condition.wait()
                    frame = self.web_streaming_output.frame

                ret = b"--FRAME\r\n"
                ret += b"Content-Type: image/jpeg\r\n"
                ret += f"Content-Length: {len(frame)}\r\n\r\n".encode()
                ret += frame
                ret += b"\r\n"
                yield ret
        except Exception as e:
            print("Removed streaming client!" + e)
