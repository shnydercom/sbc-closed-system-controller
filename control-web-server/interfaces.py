from typing import Tuple
from pydantic import BaseModel, Field
from datetime import datetime


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


class PanTilt(BaseModel):
    pan: float = Field(default=None, title="A pan value (horizontal motion)")
    tilt: float = Field(default=None, title="A tilt value (vertical motion)")
