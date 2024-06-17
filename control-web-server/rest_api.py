from flask import Flask, render_template, send_file, Blueprint
import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt

rest_api = Blueprint(
    "rest_api",
    __name__,
    url_prefix="/rest",
)


# panning
@rest_api.route("/pan-to-min")
def pan_to_min():
    return format_panning(pantilt.pan_to_min())


@rest_api.route("/pan-to-middle")
def pan_to_middle():
    return format_panning(pantilt.pan_to_middle())


@rest_api.route("/pan-to-max")
def pan_to_max():
    return format_panning(pantilt.pan_to_max())


@rest_api.route("/pan-by/<int(signed=True):relativeangle>")
def pan_by(relativeangle):
    return format_panning(pantilt.pan_by(relativeangle))


# tilting
@rest_api.route("/tilt-to-min")
def tilt_to_min():
    return format_tilting(pantilt.tilt_to_min())


@rest_api.route("/tilt-to-middle")
def tilt_to_middle():
    return format_tilting(pantilt.tilt_to_middle())


@rest_api.route("/tilt-to-max")
def tilt_to_max():
    return format_tilting(pantilt.tilt_to_max())


@rest_api.route("/tilt-by/<int(signed=True):relativeangle>")
def tilt_by(relativeangle):
    return format_tilting(pantilt.tilt_by(relativeangle))


# non-REST functions
def format_panning(angle):
    return f"<p>panning angle: {angle}</p>"


def format_tilting(angle):
    return f"<p>tilting angle: {angle}</p>"
