from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(".env")

engine = create_async_engine(os.getenv("DB_URL"), echo = True)


from shared.models import *

async def init_db():
   async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def create_db_session():
    session = AsyncSession(engine)

    try:
        yield session

    finally:
        await session.close()
