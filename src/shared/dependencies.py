from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from shared.database import create_db_session

sessionDep = Annotated[AsyncSession, Depends(create_db_session)]