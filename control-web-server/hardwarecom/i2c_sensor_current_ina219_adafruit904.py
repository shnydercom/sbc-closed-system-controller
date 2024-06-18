from interfaces import Ina219SensorReading

import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219, Mode, Gain

i2c_bus = board.I2C()

ina219A = INA219(i2c_bus, 0x41)

print("ina219 selfcheck:")

# display some of the advanced field (just to test)
print("Config register A:")
print("  bus_voltage_range:    0x%1X" % ina219A.bus_voltage_range)
print("  gain:                 0x%1X" % ina219A.gain)
print("  bus_adc_resolution:   0x%1X" % ina219A.bus_adc_resolution)
print("  shunt_adc_resolution: 0x%1X" % ina219A.shunt_adc_resolution)
print("  mode:                 0x%1X" % ina219A.mode)
print("")

# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219A.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219A.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
ina219A.bus_voltage_range = BusVoltageRange.RANGE_16V
ina219A.set_calibration_16V_400mA()


def read_current_sensor() -> Ina219SensorReading:
    bus_voltageA = ina219A.bus_voltage  # voltage on V- (load side)
    shunt_voltageA = ina219A.shunt_voltage  # voltage between V+ and V- across the shunt
    currentA = ina219A.current  # current in mA
    powerA = ina219A.power  # power in watts
    result = Ina219SensorReading(
        vin_plus_voltage=bus_voltageA + shunt_voltageA,
        bus_voltage=bus_voltageA,  # voltage on V- (load side)
        shunt_voltage=shunt_voltageA,  # voltage between V+ and V- across the shunt
        current=currentA,  # current in mA
        powerCalc=bus_voltageA * (currentA / 1000),  # power in Watts
        powerRegister=powerA,
    )
    return result
