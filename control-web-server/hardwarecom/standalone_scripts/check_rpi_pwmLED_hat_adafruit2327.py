import board
import busio
import adafruit_pca9685
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

hat.frequency = 60

led_channel_a = 15

led_channel = hat.channels[led_channel_a]
print("off")
led_channel.duty_cycle = 0x0000
sleep(3.0)
print("high")
led_channel.duty_cycle = 0xFFFF
sleep(3.0)

print("half")
led_channel.duty_cycle = 0x8888
sleep(3.0)

print("quarter")
led_channel.duty_cycle = 0x4444
sleep(3.0)

# Increase brightness:
for i in range(0xFFFF):
    led_channel.duty_cycle = i
    print(i)

# Decrease brightness:
for i in range(0xFFFF, 0, -1):
    led_channel.duty_cycle = i
    print(i)
