from flask import Flask
import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt

app = Flask(__name__)


@app.route("/")
def root_url():
    return "<p>this is the server root</p>"


# panning
@app.route("/pan-to-min")
def pan_to_min():
    return format_panning(pantilt.pan_to_min())


@app.route("/pan-to-middle")
def pan_to_middle():
    return format_panning(pantilt.pan_to_middle())


@app.route("/pan-to-max")
def pan_to_max():
    return format_panning(pantilt.pan_to_max())


@app.route("/pan-by/<int(signed=True):relativeangle>")
def pan_by(relativeangle):
    return format_panning(pantilt.pan_by(relativeangle))


# tilting
@app.route("/tilt-to-min")
def tilt_to_min():
    return format_tilting(pantilt.tilt_to_min())


@app.route("/tilt-to-middle")
def tilt_to_middle():
    return format_tilting(pantilt.tilt_to_middle())


@app.route("/tilt-to-max")
def tilt_to_max():
    return format_tilting(pantilt.tilt_to_max())


@app.route("/tilt-by/<int(signed=True):relativeangle>")
def tilt_by(relativeangle):
    return format_tilting(pantilt.tilt_by(relativeangle))


# non-REST functions
def format_panning(angle):
    return f"<p>panning angle: {angle}</p>"


def format_tilting(angle):
    return f"<p>tilting angle: {angle}</p>"
