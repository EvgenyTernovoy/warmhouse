from fastapi import FastAPI
import random
from datetime import datetime, timezone
from pydantic import BaseModel

app = FastAPI()

class TemperatureResponse(BaseModel):
    value: float
    unit: str
    timestamp: datetime
    location: str
    status: str
    sensor_id: str
    sensor_type: str
    description: str

def get_random_temperature(location: str):
    return {
  "value": random.random() * 20,
  "unit": "Celsius",
  "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
  "location": location,
  "status": "ok",
  "sensor_id": "sensor-1234-abc",
  "sensor_type": "DHT22",
  "description": "Temperature sensor near the window"
}

@app.get("/temperature", response_model=TemperatureResponse)
async def get_temperature(location: str):
    return get_random_temperature(location)

@app.get("/temperature/{location}")
async def get_temperature(location: str):
    return get_random_temperature(location)