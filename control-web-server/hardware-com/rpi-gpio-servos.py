# OOOLLLLDD Set up libraries and overall settings

#import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
#from time import sleep   # Imports sleep (aka wait or pause) into the program
#GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
#GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
#p = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin
#p.start(0)               # Starts running PWM on the pin and sets it to 0

# Move the servo back and forth
#p.ChangeDutyCycle(3)     # Changes the pulse width to 3 (so moves the servo)
#sleep(1)                 # Wait 1 second
#p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
#sleep(1)

# Clean up everything
#p.stop()                 # At the end of the program, stop the PWM
#GPIO.cleanup()           # Resets the GPIO pins back to defaults

import gpiod
LED_PIN = 17
BUTTON_PIN = 27


chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
button_line = chip.get_line(BUTTON_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
try:
   while True:
       button_state = button_line.get_value()
       if button_state == 1:
           led_line.set_value(1)
       else:
           led_line.set_value(0)
finally:
   led_line.release()
button_line.release()