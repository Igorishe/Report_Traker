import os

import telebot
from dotenv import load_dotenv

from .keyboard_services import status_keyboard, tag_keyboard
from .projects import Project

load_dotenv()

token = os.getenv('bot_token')
rs_chat = int(os.getenv('bot_chat'))
second_chat = int(os.getenv('second_bot_chat'))
refund_chat = int(os.getenv('refund_bot_chat'))
admin_id = int(os.getenv('admin_telegram'))
api_token = os.getenv('api_token')
api_host = os.getenv('api_host')
api_port = '8000'

default_api_config = {
    'host': api_host,
    'port': api_port,
    'token': api_token
}

allowed_chats = [rs_chat, second_chat, refund_chat]
allowed_users = [int(i) for i in os.getenv('allowed_users').split(',')]

bot = telebot.TeleBot(token)

RS_project = Project(
    api_config=default_api_config,
    chat=rs_chat,
    endpoint='reports',
)
MN_project = Project(
    api_config=default_api_config,
    chat=second_chat,
    endpoint='mn-reports',
)
objects = [RS_project, MN_project]

bot_commands = {
    '/rs_all': (RS_project, None, None),
    '/mn_all': (MN_project, None, None),
    '/status': (RS_project, 'status', status_keyboard()),
    '/status_mn': (MN_project, 'status', status_keyboard()),
    '/tags': (RS_project, 'tag', tag_keyboard()),
    '/tags_mn': (MN_project, 'tag', tag_keyboard()),
}


def group_access_check(message):
    """Access to function only from certain chat"""
    return message.chat.id in allowed_chats


def user_access_check(message):
    """Access to function only from certain user"""
    return message.from_user.id in allowed_users


def admin_access_check(message):
    """Access to function only from admin user"""
    return message.from_user.id == admin_id


@bot.message_handler(func=admin_access_check, commands=['group'])
def show_group(message):
    """Shows tg group id"""
    bot.send_message(
        admin_id,
        message.chat.id,
    )


@bot.message_handler(func=user_access_check, commands=['start', 'help'])
def start(message):
    """Greeting message"""
    bot.send_message(
        message.from_user.id,
        '<b>Привет! Все отчеты здесь!</b>\n\n'
        '/rs_all - все открытые отчеты по RS\n'
        '/mn_all - все открытые отчеты по MN\n'
        '/refund_all - все открытые заявки на возврат по MN\n'
        '/status - фильтр по статусам\n'
        '/status_mn - фильтр по статусам MN\n'
        '/tags - фильтр по тэгам\n'
        '/tags_mn - фильтр по тэгам MN',
        parse_mode='HTML',
    )


@bot.message_handler(func=group_access_check, content_types=['text'])
def post_report(message):
    """Saves new report"""
    project = [
        obj for obj in objects if getattr(obj, 'chat') == message.chat.id
    ][0]
    response = project.save(message=message)
    bot.send_message(
        admin_id,
        response
    )


@bot.message_handler(
    func=user_access_check,
    commands=[
        'rs_all', 'mn_all', 'refund_all', 'status', 'status_mn',
        'tags', 'tags_mn'
    ]
)
def show_reports(message):
    command = message.text
    project, backend_filter, keyboard = bot_commands[command]
    if backend_filter is not None:
        reply_message = bot.send_message(
            message.from_user.id,
            'Какие кейсы показать?',
            reply_markup=keyboard
        )
        response = project.show(
            message=reply_message,
            filter=backend_filter
        )
    else:
        response = project.show(message=message)
    bot.send_message(
        message.from_user.id,
        response,
        parse_mode='HTML',
    )
