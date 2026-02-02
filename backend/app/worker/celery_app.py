from celery import Celery
from backend.app.core.config import settings

celery_app = Celery(
    "kgoro",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

celery_app.conf.update(
    task_track_started=True,
    result_expires=3600,
)
