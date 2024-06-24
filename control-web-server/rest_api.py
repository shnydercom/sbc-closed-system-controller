from typing import List
from fastapi import APIRouter, Path
from fastapi.responses import StreamingResponse
import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt
import hardwarecom.i2c_sensor_6dof_accgyro_lsm6dsox_adafruit4438 as accgyro
import hardwarecom.i2c_sensor_current_ina219_adafruit904 as currentSensor
import hardwarecom.rpi_servohat_led_pwm_adafruit2327 as ledpwm
import hardwarecom.rpi_gpiozero_sensors_cputemp as gpio_sensors_cputemp
from hardwarecom.rpi_camera_streaming import StreamingCamera
from data_recorder import DataRecorder

# from hardwarecom.rpi_camera_module3 import StreamRecorderCamera
from interfaces import (
    AccelerometerGyroSensorReading,
    Ina219SensorReading,
    PWMDevice,
    PanTilt,
    SystemHealthReading,
    SolarChargerReading,
)
from _thread import get_ident

router = APIRouter(prefix="/rest")


inner_cam = StreamingCamera(0)
outer_cam = StreamingCamera(1)

data_recorder = DataRecorder(5, inner_cam=inner_cam, outer_cam=outer_cam)


@router.get("/start-data-recording")
def start_recorder() -> bool:
    data_recorder.trigger_start()
    return True


@router.get("/stop-data-recording")
def stop_recorder() -> bool:
    data_recorder.trigger_stop()
    return True


@router.get("/is-data-recording")
def stop_recorder() -> bool:
    return data_recorder.is_recording()


@router.get("/inner-video-stream", response_class=StreamingResponse)
def inner_video_stream():
    print("Thread %s: In inner_video_stream", get_ident())
    response = StreamingResponse(
        inner_cam.get_frame(),
        # media_type="multipart/x-mixed-replace;boundary=frame",
        headers={
            "Age": "0",
            "Cache-Control": "no-cache, private",
            "Pragma": "no-cache",
            "Content-Type": "multipart/x-mixed-replace; boundary=FRAME",
        },
    )
    return response


@router.get("/outer-video-stream", response_class=StreamingResponse)
def outer_video_stream():
    print("Thread %s: In outer_video_stream", get_ident())
    response = StreamingResponse(
        outer_cam.get_frame(),
        # media_type="multipart/x-mixed-replace;boundary=frame",
        headers={
            "Age": "0",
            "Cache-Control": "no-cache, private",
            "Pragma": "no-cache",
            "Content-Type": "multipart/x-mixed-replace; boundary=FRAME",
        },
    )
    return response


############################
# System health sensors
############################
@router.get("/system-health-sensors")
def system_health_sensors() -> SystemHealthReading:
    return SystemHealthReading(
        cpu_usage=gpio_sensors_cputemp.get_cpu_usage(),
        cpu_temp=gpio_sensors_cputemp.get_cpu_temp(),
    )


############################
# Solar charger status sensors
############################
@router.get("/solar-charger")
def solar_charger() -> SolarChargerReading:
    return SolarChargerReading(
        power_good=gpio_sensors_cputemp.get_solarcharger_powergood(),
        charging=gpio_sensors_cputemp.get_solarcharger_charging(),
    )


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
    return PWMDevice(identifier=2, strength=ledpwm.get_cooler_duty_cycle())


@router.get("/switch-cooler-off")
def switch_cooler_off() -> PWMDevice:
    ledpwm.switch_cooler_off()
    return PWMDevice(identifier=2, strength=0)


@router.get("/switch-cooler-on")
def switch_cooler_on() -> PWMDevice:
    ledpwm.switch_cooler_on()
    return PWMDevice(identifier=2, strength=1)


###


@router.get("/all-led-strengths")
def get_all_led_strengths() -> List[PWMDevice]:
    result: List[PWMDevice] = []
    for i in range(4, 16):
        result.append(PWMDevice(identifier=i, strength=ledpwm.get_led_duty_cycle(i)))
    return result


@router.post("/all-led-strengths")
def set_all_led_strengths(leds=List[PWMDevice]) -> List[PWMDevice]:
    result: List[PWMDevice] = []
    for i in range(4, 16):
        result.append(
            PWMDevice(
                identifier=i,
                strength=ledpwm.switch_led_to(
                    led_id=i,
                ),
            ),
        )
    return result


@router.get("/led-strength/{led_id}")
def led_strength(
    led_id: int = Path(title="The id of the led"),
) -> PWMDevice:
    return PWMDevice(identifier=led_id, strength=ledpwm.get_led_duty_cycle(led_id))


@router.get("/switch-led-off/{led_id}")
def switch_led_off(
    led_id: int = Path(title="The id of the led"),
) -> PWMDevice:
    strength = ledpwm.switch_led_off(led_id)
    return PWMDevice(identifier=led_id, strength=strength)


@router.get("/switch-led-on/{led_id}")
def switch_led_on(
    led_id: int = Path(title="The id of the led"),
) -> PWMDevice:
    strength = ledpwm.switch_led_on(led_id)
    return PWMDevice(identifier=led_id, strength=strength)


@router.get("/dim-led-to/{led_id}/{next_strength}")
def switch_led_to(
    led_id: int = Path(title="The id of the led"),
    next_strength: float = Path(title="The strength that the LED should change to"),
) -> PWMDevice:
    strength = ledpwm.switch_led_to(led_id, strength=next_strength)
    return PWMDevice(identifier=led_id, strength=strength)


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
