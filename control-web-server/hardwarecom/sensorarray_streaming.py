from datetime import datetime
import threading
from utils import do_every

import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt
import hardwarecom.i2c_sensor_6dof_accgyro_lsm6dsox_adafruit4438 as accgyro
import hardwarecom.i2c_sensor_current_ina219_adafruit904 as currentSensor
import hardwarecom.rpi_servohat_led_pwm_adafruit2327 as ledpwm
import hardwarecom.rpi_gpiozero_sensors_cputemp as gpio_sensors_cputemp
from hardwarecom.rpi_camera_streaming import StreamingCamera
from interfaces import SensorSummary, SolarChargerReading, SystemHealthReading


class StreamingSensorArray:
    """
    sensor_fps: sensor readings per second.
    """

    def __init__(self, sensor_fps: int):
        self.sensor_fps = sensor_fps
        self.readwrite_thread = None
        self.open_file = None

    def create_new_thread(self):
        self.readwrite_thread = threading.Thread(
            target=self._thread_fn, name="streamingsensors_thread"
        )
        csv_string = self.get_all_sensors_timestamped_flat(is_headings=True)
        self.open_file.write(csv_string)
        self.readwrite_thread.start()

    def _thread_fn(self):
        fps_in_s = 1 / self.sensor_fps
        try:
            self._readwrite_sensors(self.open_file)
            do_every(fps_in_s, self._readwrite_sensors, self.open_file)
        except ValueError as ve:
            # print("val error" + str(ve))
            return
        except Exception as e:
            # print("other Exc" + str(e))
            return
        finally:
            # print("finally")
            return

    def get_all_sensors_timestamped(self) -> SensorSummary:
        result = SensorSummary(
            currentSensor=currentSensor.read_current_sensor(),
            accgyroSensor=accgyro.read_accelerometer_and_gyro_sensor(),
            systemHealth=SystemHealthReading(
                cpu_usage=gpio_sensors_cputemp.get_cpu_usage(),
                cpu_temp=gpio_sensors_cputemp.get_cpu_temp(),
            ),
            chargerSensor=SolarChargerReading(
                power_good=gpio_sensors_cputemp.get_solarcharger_powergood(),
                charging=gpio_sensors_cputemp.get_solarcharger_charging(),
            ),
        )
        return result

    def get_all_sensors_timestamped_flat(self, is_headings: bool = False):
        dict = {
            "dateTime": datetime.now(),
            **currentSensor.read_current_sensor_flat(),
            **accgyro.read_accelerometer_and_gyro_sensor_flat(),
            "cpu_usage": gpio_sensors_cputemp.get_cpu_usage(),
            "cpu_temp": gpio_sensors_cputemp.get_cpu_temp(),
            "power_good": gpio_sensors_cputemp.get_solarcharger_powergood(),
            "charging": gpio_sensors_cputemp.get_solarcharger_charging(),
        }
        result = ""
        for key, value in dict.items():
            if not is_headings:
                result += str(value) + "\t"
            else:
                result += str(key) + "\t"
        return result

    def _readwrite_sensors(self, open_file_in_thread):
        # sensor_readings = StringIO(
        #    str(self.get_all_sensors_timestamped().model_dump_json())
        # )
        # print(str(self.get_all_sensors_timestamped().model_dump_json()))
        # df = pd.read_json(
        #    sensor_readings,
        # )
        csv_string = "\n" + self.get_all_sensors_timestamped_flat()
        if open_file_in_thread.writable() and not self.closing:
            try:
                open_file_in_thread.write(csv_string)
            except Exception as e:
                print(str(e))
        else:
            raise ValueError("writing file ends")

    def start_recording(self, output_filename):
        self.closing = False
        self.open_file = open(file=output_filename + ".csv", mode="x")
        self.create_new_thread()
        # print("starting")

    def stop_recording(self):
        # print("call stop_rec")
        self.closing = True
        self.readwrite_thread.join(0.1)
        self.open_file.close()
        # print("is_alive" + str(self.readwrite_thread.is_alive()))
        # print("stopping")
