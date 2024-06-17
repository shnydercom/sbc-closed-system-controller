# documentation here: https://pypi.org/project/gpiod/
# doesn't seem to work yet, preferring gpiozero
import gpiod
from gpiod.line import Direction, Value, Drive, Edge
import time

with gpiod.Chip("/dev/gpiochip4") as chip:
    info = chip.get_info()
    print(f"{info.name} [{info.label}] ({info.num_lines} lines)")

PGOOD_PIN = 20  # purple
CHG_PIN = 21
chip = gpiod.Chip("/dev/gpiochip4")

####
###    NOT WORKING WELL!!!
####
with gpiod.request_lines(
    "/dev/gpiochip4",
    consumer="blink-example",
    config={
        PGOOD_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            drive=Drive.PUSH_PULL,
            active_low=True,
        ),
        CHG_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
            drive=Drive.PUSH_PULL,
            active_low=True,
            edge_detection=Edge.BOTH,
        ),
    },
) as request:
    while True:
        [pgood_value, chg_value] = request.get_values([PGOOD_PIN, CHG_PIN])
        print("power good: {}".format(pgood_value))
        print("charging: {}".format(chg_value))
        time.sleep(0.1)
