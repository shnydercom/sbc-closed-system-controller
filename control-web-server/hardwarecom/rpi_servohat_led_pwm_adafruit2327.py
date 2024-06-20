import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(i2c=i2c, channels=16)

# pin on the 16-channel servo pwm used for controlling an additional cooler
cooler_id = 2


#####################
# additional pwm cooler speed adjustment:
#####################
def get_cooler_duty_cycle():
    return hat.channels[cooler_id].duty_cycle


def switch_cooler_off():
    hat.channels[cooler_id].duty_cycle = 0x0000


def switch_cooler_on():
    hat.channels[cooler_id].duty_cycle = 0xFFFF


#####################
# LED pwm switching
#####################

# pins on the 16-channel servo pwm used for LEDs
acceptable_led_ids = range(4, 16)


def get_led_duty_cycle(led_id: int):
    if led_id in acceptable_led_ids:
        return hat.channels[led_id].duty_cycle
    raise ValueError("led_id was out of acceptable range")


def switch_led_off(led_id: int) -> float:
    if led_id in acceptable_led_ids:
        hat.channels[led_id].duty_cycle = 0x0000
        return 0
    raise ValueError("led_id was out of acceptable range")


def switch_led_on(led_id: int) -> float:
    if led_id in acceptable_led_ids:
        hat.channels[led_id].duty_cycle = 0xFFFF
        return 1
    raise ValueError("led_id was out of acceptable range")


def switch_led_to(led_id: int, strength: float) -> float:
    if strength > 1 or strength < 0:
        raise ValueError("strength must be between 0 and 1 (100%)")
    if led_id in acceptable_led_ids:
        newstrength: int = int(strength * 65535)
        hat.channels[led_id].duty_cycle = newstrength
        return newstrength / 65535
    raise ValueError("led_id was out of acceptable range")
