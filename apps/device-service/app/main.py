from fastapi import FastAPI, HTTPException, Path, Depends
from fastapi.responses import JSONResponse
from app.models.sensor import Sensors, SensorType
from app.db.db import async_session, init_db, get_sensor_by_id
from typing import AsyncGenerator
from sqlmodel.ext.asyncio.session import AsyncSession
import httpx
import logging
import os

app = FastAPI()

temperature_api_url = os.environ.get("TEMPERATURE_API_URL", "http://127.0.0.1:8081")

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

# Initialize DB on startup
@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/api/v2/sensors/{id}", response_model=Sensors)
async def read_sensor_by_id(id: int, session: AsyncSession = Depends(get_session)):
    try:
        sensor = await get_sensor_by_id(session, id)
        if not sensor:
            raise HTTPException(status_code=404, detail="Sensor not found")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid sensor ID")

    # Если тип сенсора — temperature, получаем внешние данные
    if sensor.type == SensorType.temperature:
        try:
            async with httpx.AsyncClient() as client:
                url = f"{temperature_api_url}/temperature/{sensor.id}"
                response = await client.get(url)
                response.raise_for_status()
                temp_data = response.json()

                # Обновление значений сенсора
                sensor.value = temp_data["value"]
                sensor.status = temp_data["status"]
                sensor.last_updated = temp_data["timestamp"]

                logging.info(f"Updated temperature data for sensor {sensor.id} from external API")

        except Exception as e:
            logging.warning(f"Failed to fetch temperature data for sensor {sensor.id}: {e}")

    return sensor