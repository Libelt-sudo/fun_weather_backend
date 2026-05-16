import os
from celery import Celery
from celery.schedules import schedule, crontab

app = Celery(
    "sms_sender",
    broker = os.getenv("CELERY_BROKER_URL")
)

app.conf.include = ["src.sms_service.tasks"]

app.conf.beat_schedule = {
    "sms_sender":{
        "task": "src.sms_service.tasks.send_sms_all",
        "schedule": schedule(5.0)
    }
}

