import board
import busio
import adafruit_pca9685
from time import sleep
from adafruit_servokit import ServoKit

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)


kit = ServoKit(i2c=i2c, channels=16)

led_channel_a = 15
# additional cooler speed adjustment:
hat.channels[2].duty_cycle = 0x0000
while True:
    # Increase brightness:
    for i in range(4, 16):
        print(i)
        led_channel = hat.channels[i]
        print("off")
        led_channel.duty_cycle = 0x0000
        kit.servo[0].angle = 0
        kit.servo[1].angle = 0
        sleep(0.5)
        print("high")
        led_channel.duty_cycle = 0xFFFF
        kit.servo[0].angle = 0
        kit.servo[1].angle = 0
        sleep(0.5)
