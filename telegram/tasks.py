import os

from dotenv import load_dotenv
from telebot.apihelper import send_message

from traker.celery import app

load_dotenv()

admin_id = os.getenv('admin_telegram')
token = os.getenv('bot_token')

@app.task
def send_notify(text):
    send_message(
        token,
        admin_id,
        text,
    )


@app.task
def send_beat_notify():
    send_message(
        token,
        admin_id,
        'Periodic notify',
    )
