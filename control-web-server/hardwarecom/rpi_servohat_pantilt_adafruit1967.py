from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# CONFIG:
# cam turning (pan): channel 1
# cam nodding (tilt): channel 0

turner_id = 1
nodder_id = 0

turner_max_range = 120
nodder_max_range = 120

kit.servo[nodder_id].actuation_range = nodder_max_range
kit.servo[turner_id].actuation_range = turner_max_range


def tilt_to_min():
    new_angle = 0
    return tilt_angle(new_angle)


def tilt_to_middle():
    new_angle = nodder_max_range / 2
    return tilt_angle(new_angle)


def tilt_to_max():
    new_angle = nodder_max_range
    return tilt_angle(new_angle)


def tilt_by(relative_angle: float):
    new_angle = kit.servo[nodder_id].angle + round(relative_angle)
    if new_angle > nodder_max_range:
        new_angle = nodder_max_range
    if new_angle < 0:
        new_angle = 0
    return tilt_angle(new_angle)


def pan_to_min():
    new_angle = 0
    return pan_angle(new_angle)


def pan_to_middle():
    new_angle = turner_max_range / 2
    return pan_angle(new_angle)


def pan_to_max():
    new_angle = turner_max_range
    return pan_angle(new_angle)


def pan_by(relative_angle: float):
    new_angle = kit.servo[turner_id].angle + round(relative_angle)
    if new_angle > turner_max_range:
        new_angle = turner_max_range
    if new_angle < 0:
        new_angle = 0
    return pan_angle(new_angle)


def pan_angle(absolute_angle):
    """
    function for internal use to return the target angle and perform the servo motion
    """
    kit.servo[turner_id].angle = absolute_angle
    return absolute_angle


def tilt_angle(absolute_angle):
    """
    function for internal use to return the target angle and perform the servo motion
    """
    kit.servo[nodder_id].angle = absolute_angle
    return absolute_angle
