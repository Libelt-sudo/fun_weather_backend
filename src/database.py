from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from dotenv import load_dotenv
import os

load_dotenv(".env")


Base = declarative_base()

engine = create_async_engine(os.getenv("DB_URL"), echo = True)


async def create_db_session():
    with AsyncSession(engine) as session:
        yield session
