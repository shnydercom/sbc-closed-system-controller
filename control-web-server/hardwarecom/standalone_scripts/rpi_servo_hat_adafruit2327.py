# Product: https://www.adafruit.com/product/2327
# Tutorial: https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/
# Tutorial actually means this command:  `pip3 install adafruit-circuitpython-servokit`
# Tutorial actually means this installation of blinka: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
# Code part of the tutorial: https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/using-the-python-library

from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

# test bed, runs through angles and some demo code
servo_id = 0
max_range = 120

# more or less soft rotation
# range_step = 1
# sleep_time = 0.01

# skipping in 30 degree steps, relatively smooth
range_step = 30
sleep_time = 0.7

# kit.continuous_servo[1].throttle = 1
# kit.continuous_servo[1].throttle = -0.1

# kit.servo[servo_id].actuation_range = max_range
# kit.servo[servo_id].angle = 0
# kit.servo[servo_id].angle = 180
# kit.servo[servo_id].angle = 90
# kit.servo[servo_id].angle = 30
# kit.servo[servo_id].angle = 0
# kit.servo[servo_id].set_pulse_width_range(000, 5000)
while True:
    for rotation in range(0, max_range, range_step):
        kit.servo[0].angle = rotation
        kit.servo[1].angle = rotation
        print(rotation)
        sleep(sleep_time)

    for rotation in range(0, max_range, range_step):
        kit.servo[0].angle = max_range - rotation
        kit.servo[1].angle = max_range - rotation
        print(max_range - rotation)
        sleep(sleep_time)

    # rotations to get full maxium range of motion (avoid obstacles while building)
    for rotation in range(0, max_range, range_step):
        kit.servo[0].angle = rotation
        print(rotation)
        sleep(sleep_time)

    for rotation in range(0, max_range, range_step):
        kit.servo[1].angle = rotation
        print(rotation)
        sleep(sleep_time)

    for rotation in range(0, max_range, range_step):
        kit.servo[0].angle = max_range - rotation
        print(max_range - rotation)
        sleep(sleep_time)

    for rotation in range(0, max_range, range_step):
        kit.servo[1].angle = max_range - rotation
        print(max_range - rotation)
        sleep(sleep_time)
