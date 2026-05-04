from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from .database import create_db_session

sessionDep = Annotated[AsyncSession, create_db_session()]