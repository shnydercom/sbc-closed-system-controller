from typing import Tuple
from pydantic import BaseModel, Field
from datetime import datetime


class SystemHealthReading(BaseModel):
    cpu_temp: float
    cpu_usage: float


class SolarChargerReading(BaseModel):
    power_good: float
    charging: float


class AccelerometerGyroSensorReading(BaseModel):
    acceleration: Tuple[float, float, float]
    gyro: Tuple[float, float, float]


class Ina219SensorReading(BaseModel):
    vin_plus_voltage: float  # Volt
    bus_voltage: float  # Volt
    shunt_voltage: float  # Volt
    current: float  # milliAmps
    powerCalc: float  # Watt
    powerRegister: float  # Watt


class SensorSummary(BaseModel):
    dateTime: datetime = Field(
        default=datetime.now(),
        title="the current date and time by default. Timestamp of the sensor readings",
    )
    currentSensor: Ina219SensorReading
    accgyroSensor: AccelerometerGyroSensorReading
    systemHealth: SystemHealthReading
    chargerSensor: SolarChargerReading


class PanTilt(BaseModel):
    pan: float = Field(default=None, title="A pan value (horizontal motion)")
    tilt: float = Field(default=None, title="A tilt value (vertical motion)")


class PWMDevice(BaseModel):
    identifier: int = Field(
        default=None, title="A value to uniquely identify the device among others"
    )
    strength: float = Field(
        default=0, title="how much of the duty cycle is 1 instead of 0"
    )
