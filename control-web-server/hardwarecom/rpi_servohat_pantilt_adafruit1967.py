from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

# CONFIG:
# cam turning (pan): channel 0
# cam nodding (tilt): channel 1

turner_id = 1
nodder_id = 0

turner_max_range = 120
nodder_max_range = 120

kit.servo[nodder_id].actuation_range = nodder_max_range
kit.servo[turner_id].actuation_range = turner_max_range


def tilt_to_min():
    kit.servo[nodder_id].angle = 0
    return True


def tilt_to_middle():
    kit.servo[nodder_id].angle = nodder_max_range / 2
    return True


def tilt_to_max():
    kit.servo[nodder_id].angle = nodder_max_range
    return True


def tilt_by(relative_angle):
    new_angle = kit.servo[nodder_id].angle + relative_angle
    if new_angle > nodder_max_range:
        return False
    if new_angle < 0:
        return False
    kit.servo[nodder_id].angle = new_angle
    return True


def pan_to_min():
    kit.servo[turner_id].angle = 0
    return True


def pan_to_middle():
    kit.servo[turner_id].angle = turner_max_range / 2
    return True


def pan_to_max():
    kit.servo[turner_id].angle = turner_max_range
    return True


def pan_by(relative_angle):
    new_angle = kit.servo[turner_id].angle + relative_angle
    if new_angle > turner_max_range:
        return False
    if new_angle < 0:
        return False
    kit.servo[turner_id].angle = new_angle
    return True
