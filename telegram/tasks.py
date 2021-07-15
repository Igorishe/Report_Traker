import os

from dotenv import load_dotenv

from traker.celery import app
# from .services.bot_manage import bot

load_dotenv()

admin_id = os.getenv('admin_telegram')


'''@app.task
def send_message(text):
    bot.send_message(
        admin_id,
        text,
    )'''


@app.task
def send_message(text):
    print(text)
