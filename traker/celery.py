import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traker.settings')

app = Celery('traker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'notify-every-morning': {
        'task': 'telegram.tasks.send_beat_notify',
        'schedule': crontab(minute=0, hour=8, day_of_week='mon-fri'),
    },
    'notify-burn-reports': {
        'task': 'telegram.tasks.burning_notify',
        'schedule': crontab(minute=0, hour=13, day_of_week='mon-fri'),
    },
    'update-statuses': {
        'task': 'reports.tasks.update_statuses',
        'schedule': crontab(minute=0, hour=15),
    },
    'update-tags': {
        'task': 'reports.tasks.update_tags',
        'schedule': crontab(minute=0, hour=15),
    },
}
