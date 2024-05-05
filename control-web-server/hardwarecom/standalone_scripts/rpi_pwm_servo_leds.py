import board
import busio
import adafruit_pca9685
from time import sleep
from adafruit_servokit import ServoKit

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)


kit = ServoKit(i2c=i2c, channels=16)

led_channel_a = 15
while True:
    led_channel = hat.channels[led_channel_a]
    print("off")
    led_channel.duty_cycle = 0x0000
    kit.servo[0].angle = 0
    kit.servo[1].angle = 0
    sleep(2.0)
    print("high")
    led_channel.duty_cycle = 0xFFFF
    kit.servo[0].angle = 180
    kit.servo[1].angle = 180
    sleep(2.0)
