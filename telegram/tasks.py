import os

from dotenv import load_dotenv
from reports.models import Report
from telebot.apihelper import send_message

from traker.celery import app

load_dotenv()

admin_id = int(os.getenv('admin_telegram'))
moderator_id = int(os.getenv('moderator_telegram'))
notify_users = [admin_id, moderator_id]
token = os.getenv('bot_token')


def report_count(queryset):
    all = queryset.count()
    new = queryset.filter(status='New').count()
    burning = queryset.filter(tag='Burning').count()
    forgotten = queryset.filter(tag='Forgotten').count()
    output = (
        'Привет! Посмотри, какие вопросы сейчас актуальны!\n\n'
        f'Всего вопросов: <b>{all}</b>\n'
        f'Новых вопросов: <b>{new}</b>\n'
        f'Срочных вопросов: <b>{burning}</b>\n'
        f'Забытых вопросов: <b>{forgotten}</b>\n\n'
        '<b>Удачи!</b>'
    )
    return output


@app.task
def send_notify():
    reports = Report.objects.all()
    output = report_count(reports)
    send_message(
        token,
        admin_id,
        output,
        parse_mode='HTML',
    )


@app.task
def send_beat_notify():
    reports = Report.objects.all()
    output = report_count(reports)
    for user in notify_users:
        send_message(
            token,
            user,
            output,
            parse_mode='HTML',
        )
