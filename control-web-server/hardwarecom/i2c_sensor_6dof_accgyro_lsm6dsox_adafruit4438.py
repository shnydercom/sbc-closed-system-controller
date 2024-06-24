import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
from interfaces import AccelerometerGyroSensorReading

i2c = board.I2C()
sensor = LSM6DSOX(i2c)


def read_accelerometer_and_gyro_sensor() -> AccelerometerGyroSensorReading:
    result = AccelerometerGyroSensorReading(
        acceleration=sensor.acceleration, gyro=sensor.gyro
    )
    return result


def read_accelerometer_and_gyro_sensor_flat():
    result = {"acceleration": str(sensor.acceleration), "gyro": str(sensor.gyro)}
    return result
