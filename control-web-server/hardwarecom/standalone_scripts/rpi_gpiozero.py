from gpiozero import InputDevice
import time

PGOOD_PIN = 20  # purple
CHG_PIN = 21

pgood_input = InputDevice(pin=PGOOD_PIN, pull_up=None, active_state=False)
pgood_chg = InputDevice(pin=CHG_PIN, pull_up=None, active_state=False)

while True:
    [pgood_value, chg_value] = [pgood_input.value, pgood_chg.value]
    print("power good: {}".format(pgood_value))
    print("charging: {}".format(chg_value))
    time.sleep(1)
