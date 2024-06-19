from fastapi import APIRouter, Path
import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt
import hardwarecom.i2c_sensor_6dof_accgyro_lsm6dsox_adafruit4438 as accgyro
import hardwarecom.i2c_sensor_current_ina219_adafruit904 as currentSensor
import hardwarecom.rpi_servohat_led_pwm_adafruit2327 as ledpwm
from interfaces import (
    AccelerometerGyroSensorReading,
    Ina219SensorReading,
    PWMDevice,
    PanTilt,
)

router = APIRouter(prefix="/rest")


############################
# 6DOF Accelerometer sensor
############################
@router.get("/accelerometer-gyro-sensor")
def accelerometer_gyro_sensor() -> AccelerometerGyroSensorReading:
    return accgyro.read_accelerometer_and_gyro_sensor()


############################
# ina219 high side current sensor
############################
@router.get("/current-sensor")
def current_sensor() -> Ina219SensorReading:
    return currentSensor.read_current_sensor()


############################
# LED and cooler control
############################
@router.get("/cooler-strength")
def cooler_strength() -> PWMDevice:
    return ledpwm.get_cooler_duty_cycle()


@router.get("/switch-cooler-off")
def switch_cooler_off() -> PWMDevice:
    ledpwm.switch_cooler_off()
    return PWMDevice(strength=0)


@router.get("/switch-cooler-on")
def switch_cooler_on() -> PWMDevice:
    ledpwm.switch_cooler_on()
    return PWMDevice(strength=1)


###


@router.get("/led-strength/{led_id}")
def led_strength(
    led_id: int = Path(title="The id of the led"),
) -> PWMDevice:
    return ledpwm.get_led_duty_cycle(led_id)


@router.get("/switch-led-off/{led_id}")
def switch_led_off(
    led_id: int = Path(title="The id of the led"),
) -> PWMDevice:
    strength = ledpwm.switch_led_off(led_id)
    return PWMDevice(strength)


@router.get("/switch-led-on/{led_id}")
def switch_led_on(
    led_id: int = Path(title="The id of the led"),
) -> PWMDevice:
    strength = ledpwm.switch_led_on(led_id)
    return PWMDevice(strength)


@router.get("/dim-led-to/{led_id}/{next_strength}")
def switch_led_on(
    led_id: int = Path(title="The id of the led"),
    next_strength: int = Path(title="The strength that the LED should change to"),
) -> PWMDevice:
    strength = ledpwm.switch_led_to(led_id, strength=next_strength)
    return PWMDevice(strength)


############################
# Panning and tilting control
############################

currentOrientation = PanTilt(pan=pantilt.pan_to_middle(), tilt=pantilt.tilt_to_middle())


@router.get("/pantilt-orientation")
def pantilt_orientation() -> PanTilt:
    return currentOrientation


# panning
@router.get("/pan-to-min")
def pan_to_min() -> PanTilt:
    currentOrientation.pan = pantilt.pan_to_min()
    return currentOrientation


@router.get("/pan-to-middle")
def pan_to_middle() -> PanTilt:
    currentOrientation.pan = pantilt.pan_to_middle()
    return currentOrientation


@router.get("/pan-to-max")
def pan_to_max() -> PanTilt:
    currentOrientation.pan = pantilt.pan_to_max()
    return currentOrientation


@router.get("/pan-by/{relativeangle}")
def pan_by(
    relativeangle: int = Path(title="The angle in degrees for relative movement"),
) -> PanTilt:
    currentOrientation.pan = pantilt.pan_by(relativeangle)
    return currentOrientation


# tilting
@router.get("/tilt-to-min")
def tilt_to_min() -> PanTilt:
    currentOrientation.tilt = pantilt.tilt_to_min()
    return currentOrientation


@router.get("/tilt-to-middle")
def tilt_to_middle() -> PanTilt:
    currentOrientation.tilt = pantilt.tilt_to_middle()
    return currentOrientation


@router.get("/tilt-to-max")
def tilt_to_max() -> PanTilt:
    currentOrientation.tilt = pantilt.tilt_to_max()
    return currentOrientation


@router.get("/tilt-by/{relativeangle}")
def tilt_by(
    relativeangle: int = Path(title="The angle in degrees for relative movement"),
) -> PanTilt:
    currentOrientation.tilt = pantilt.tilt_by(relativeangle)
    return currentOrientation
