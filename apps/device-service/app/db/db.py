from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker
from typing import Optional
from app.models.sensor import Sensors  # модель SQLModel для Sensor
from sqlalchemy.exc import NoResultFound
import logging
import os

# PostgreSQL connection URL
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/smarthome")

# Create SQLModel engine
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_sensor_by_id(session: AsyncSession, sensor_id: int) -> Optional[Sensors]:
    try:
        statement = select(Sensors).where(Sensors.id == sensor_id)
        result = await session.exec(statement)
        sensor = result.one()
        logging.info(f"Getting sensor by ID {sensor}")
        return sensor
    except NoResultFound:
        return None
    except Exception as e:
        logging.error(f"Error getting sensor by ID {sensor_id}: {e}")
        raise
