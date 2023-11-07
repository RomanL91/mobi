import os
from celery import Celery
# from celery.schedules import crontab
from core.settings import CELERY_BROKER_URL

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery(
    main='core',
    broker_connection_retry_on_startup=True,
    broker=CELERY_BROKER_URL,
    include=['app_products.tasks'],
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every': { 
        'task': 'app_products.tasks.check_discount_period',
        # 'schedule': crontab(minute=1),
        'schedule': 3600.0,
    }, 
}

if __name__ == '__main__':
    app.start()
