from gpiozero import CPUTemperature, InputDevice
import psutil

#####################
# Single Board Computer system health
#####################

cpu = CPUTemperature()
# gives a single float value
cpu_usage = psutil.cpu_percent()

print("SBC system health at start:")
print("  CPU temperature:    " + str(cpu.temperature))
print("  CPU usage      :    " + str(cpu_usage))


def get_cpu_temp():
    return cpu.temperature


def get_cpu_usage():
    return psutil.cpu_percent()


#####################
# solar charger status readings
#####################

PGOOD_PIN = 20  # purple wire
CHG_PIN = 21  # blue wire

pgood_input = InputDevice(pin=PGOOD_PIN, pull_up=None, active_state=False)
pgood_chg = InputDevice(pin=CHG_PIN, pull_up=None, active_state=False)


def get_solarcharger_powergood():
    return pgood_input.value


def get_solarcharger_charging():
    return pgood_chg.value
