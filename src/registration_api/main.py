from typing import Annotated, List

from contextlib import asynccontextmanager
from fastapi import FastAPI, Body, Depends, Path, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shared.database import init_db
from schemas import SubscriberCreate, SubscriberResponse
from shared.models import Subscriber
from shared.dependencies import sessionDep


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/register",response_model=SubscriberResponse, status_code=201)
async def register_sub(sub: Annotated[SubscriberCreate, Body()], session: sessionDep):
    
    new_subscriber = Subscriber(email=sub.email, phone_number=sub.phone_number)

    session.add(new_subscriber)
    await session.commit()
    
    await session.refresh(new_subscriber)

    return new_subscriber


@app.delete("/unregister/{email}", status_code=204)
async def unregister_sub(email: Annotated[str, Path()], session: sessionDep):
    result = await session.execute(select(Subscriber).where(Subscriber.email == email))
    sub = result.scalar_one_or_none()

    if sub is None:
        raise HTTPException(404, detail="Subscriber not found.")

    await session.delete(sub)
    await session.commit()

    return {"message": f"Subscriber {email} successfully removed."}


@app.get("/get_subs")
async def get_subs(session: sessionDep) -> List[SubscriberResponse]:

    result = await session.scalars(select(Subscriber))
    subs = result.all()

    return subs