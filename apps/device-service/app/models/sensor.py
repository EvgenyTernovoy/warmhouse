from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class SensorType(str, Enum):
    temperature = "temperature"

class Sensors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    type: SensorType
    location: str
    value: float
    unit: str
    status: str
    last_updated: datetime
    created_at: datetime