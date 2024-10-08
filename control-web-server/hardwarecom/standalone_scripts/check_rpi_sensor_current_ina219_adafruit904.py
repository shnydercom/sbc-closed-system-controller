# command to install dependency: https://pypi.org/project/adafruit-circuitpython-ina219/
# code tutorial: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython#full-example-code-2997919

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Sample code and test for adafruit_ina219"""

import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219, Mode, Gain

i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ina219A = INA219(i2c_bus, 0x41)  # address changed by soldering A0
# ina219B = INA219(i2c_bus, 0x44)

print("ina219 test")

# display some of the advanced field (just to test)
print("Config register A:")
print("  bus_voltage_range:    0x%1X" % ina219A.bus_voltage_range)
print("  gain:                 0x%1X" % ina219A.gain)
print("  bus_adc_resolution:   0x%1X" % ina219A.bus_adc_resolution)
print("  shunt_adc_resolution: 0x%1X" % ina219A.shunt_adc_resolution)
print("  mode:                 0x%1X" % ina219A.mode)
print("")

## Sensor B is dead, after showing increasingly wrong(er) data
"""
# display some of the advanced field (just to test)
print("Config register B:")
print("  bus_voltage_range:    0x%1X" % ina219B.bus_voltage_range)
print("  gain:                 0x%1X" % ina219B.gain)
print("  bus_adc_resolution:   0x%1X" % ina219B.bus_adc_resolution)
print("  shunt_adc_resolution: 0x%1X" % ina219B.shunt_adc_resolution)
print("  mode:                 0x%1X" % ina219B.mode)
print("")
# exit()
"""
# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
# ina219A.bus_adc_resolution = ADCResolution.ADCRES_12BIT_2S
# ina219A.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_2S
# optional : change voltage range to 16V
# ina219A.bus_voltage_range = BusVoltageRange.RANGE_16V
# ina219A.set_calibration_16V_5A()
"""
# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219B.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219B.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
ina219B.bus_voltage_range = BusVoltageRange.RANGE_16V
ina219B.mode = Mode.

ina219B.set_calibration_32V_1A()"""

# measure and display loop
while True:
    bus_voltageA = ina219A.bus_voltage  # voltage on V- (load side)
    shunt_voltageA = ina219A.shunt_voltage  # voltage between V+ and V- across the shunt
    currentA = ina219A.current  # current in mA
    powerA = ina219A.power  # power in watts
    raw_current = ina219A.raw_current

    # ina219A measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print("A:")
    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltageA + shunt_voltageA))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltageA))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltageA))
    print("Shunt Current  : {:7.5f}  mA".format(currentA))
    print("Power Calc.    : {:8.5f} W".format(bus_voltageA * (currentA / 1000)))
    print("Power Register : {:6.3f}   W".format(powerA))

    print("Raw current    : {:6.5f}   mA".format(raw_current))
    print("B:")

    # Check internal calculations haven't overflowed (doesn't detect ADC overflows)
    if ina219A.overflow:
        print("Internal Math Overflow Detected!")
        print("")

    # B experienced bit shifting problems: https://forums.raspberrypi.com/viewtopic.php?t=286270
    """
    bus_voltageB = ina219B.bus_voltage  # voltage on V- (load side)
    shunt_voltageB = ina219B.shunt_voltage  # voltage between V+ and V- across the shunt
    currentB = ina219B.current  # current in mA
    powerB = ina219B.power  # power in watts

    # ina219B measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltageB + shunt_voltageB))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltageB))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltageB))
    print("Shunt Current  : {:7.4f}  A".format(currentB / 1000))
    print("Power Calc.    : {:8.5f} W".format(bus_voltageB * (currentB / 1000)))
    print("Power Register : {:6.3f}   W".format(powerB))
    print("")
    print(f"{ina219B.raw_current:16b}")
    print(f"{ina219B.raw_shunt_voltage:16b}")
    print("")

    # Check internal calculations haven't overflowed (doesn't detect ADC overflows)
    if ina219B.overflow:
        print("Internal Math Overflow Detected!")
        print("")
    """
    time.sleep(0.1)
