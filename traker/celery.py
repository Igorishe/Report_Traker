import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traker.settings')

app = Celery('traker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
