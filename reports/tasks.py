from datetime import timedelta, datetime

from django.utils import timezone

from .models import Report
from traker.celery import app


def update_reports(period, status=None, tag=None):
    lookup_date = timezone.now() - timedelta(hours=period)
    if status:
        key = 'status'
        value = status
        update_value = 'Actual'
    if tag:
        key = 'tag'
        value = tag
        update_value = 'Forgotten'
    reports = Report.objects.filter(
        date__lt=lookup_date).filter(**{key: value}).exclude(status='Closed')
    reports.update(**{key: update_value})


@app.task
def update_statuses():
    update_reports(24, status='New')


@app.task
def update_tags():
    tags_time = {
        'Burning': 24,
        'Normal': 48,
        'Delayed': 72,
    }
    for key, value in tags_time.items():
        update_reports(value, tag=key)
