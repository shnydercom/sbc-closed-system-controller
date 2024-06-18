from fastapi import APIRouter, Path
from pydantic import BaseModel

import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt

router = APIRouter(prefix="/rest")


class PanTilt(BaseModel):
    pan: float
    tilt: float


currentOrientation = PanTilt(pan=pantilt.pan_to_middle(), tilt=pantilt.tilt_to_middle())


@router.get("/pantilt-orientation")
def pantilt_orientation():
    return currentOrientation


# panning
@router.get("/pan-to-min")
def pan_to_min():
    currentOrientation.pan = pantilt.pan_to_min()
    return currentOrientation
    # return format_panning(pantilt.pan_to_min())


@router.get("/pan-to-middle")
def pan_to_middle():
    currentOrientation.pan = pantilt.pan_to_middle()
    return currentOrientation
    # return format_panning(pantilt.pan_to_middle())


@router.get("/pan-to-max")
def pan_to_max():
    currentOrientation.pan = pantilt.pan_to_max()
    return currentOrientation
    # return format_panning(pantilt.pan_to_max())


# @router.get("/pan-by/<int(signed=True):relativeangle>")
@router.get("/pan-by/{relativeangle}")
def pan_by(
    relativeangle: int = Path(title="The angle in degrees for relative movement"),
):
    currentOrientation.pan = pantilt.pan_by(relativeangle)
    return currentOrientation
    # return format_panning(pantilt.pan_by(relativeangle))


# tilting
@router.get("/tilt-to-min")
def tilt_to_min():
    currentOrientation.tilt = pantilt.tilt_to_min()
    return currentOrientation
    # return format_tilting(pantilt.tilt_to_min())


@router.get("/tilt-to-middle")
def tilt_to_middle():
    currentOrientation.tilt = pantilt.tilt_to_middle()
    return currentOrientation
    # return format_tilting(pantilt.tilt_to_middle())


@router.get("/tilt-to-max")
def tilt_to_max():
    currentOrientation.tilt = pantilt.tilt_to_max()
    return currentOrientation
    # return format_tilting(pantilt.tilt_to_max())


# @router.get("/tilt-by/<int(signed=True):relativeangle>")
@router.get("/tilt-by/{relativeangle}")
def tilt_by(
    relativeangle: int = Path(title="The angle in degrees for relative movement"),
):
    currentOrientation.tilt = pantilt.tilt_by(relativeangle)
    return currentOrientation
    # return format_tilting(pantilt.tilt_by(relativeangle))


# non-REST functions
def format_panning(angle):
    return f"<p>panning angle: {angle}</p>"


def format_tilting(angle):
    return f"<p>tilting angle: {angle}</p>"
