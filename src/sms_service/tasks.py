import os
import json
import redis
from sqlalchemy import select
from celery_app import app
from celery.schedules import schedule, crontab
from third_party import get_weather, get_joke
from shared.database import AsyncSessionLocal
from shared.models import Subscriber



todays_weather = get_weather()

cache = redis.Redis(host= os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")))

def weather_cache():
    weather = get_weather()
    cache.set("todays_weather", json.dump(weather))


async def get_subs():
    async with AsyncSessionLocal as session:
        result = await session.execute(select(Subscriber))
        return result.scalars().all()


def send_sms_sub(phone_number: int):
    joke_str = get_joke()
    weather = json.loads(cache.get("todays_weather"))
    sms_text = f"HELLO! 😁 \nToday's weather in London is currently {weather.temp}, but feels like {weather.feels_like}. \n\n{joke_str} 😂"

    print(sms_text)


@app.task
def send_sms_all():
    subs = get_subs

    for sub in subs:
        send_sms_sub(sub.phone_number)


app.conf.beat_schedule = {
    "sms-sender": {
        "task": "tasks.send_sms_all",
        "schedule": schedule(10.0)
    }
}

app.conf.timezone = "Europe/London"
app.conf.enable_utc = True