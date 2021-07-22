import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traker.settings')

app = Celery('traker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'notify-every-minute': {
        'task': 'telegram.tasks.send_beat_notify',
        'schedule': crontab(minute=55, hour=15),
    },
    'update-statuses': {
        'task': 'reports.tasks.update_statuses',
        'schedule': crontab(minute=22, hour=14),
    },
    'update-tags': {
        'task': 'reports.tasks.update_tags',
        'schedule': crontab(minute=23, hour=14),
    },
}
