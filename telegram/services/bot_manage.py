import os

import telebot
from dotenv import load_dotenv

from .ex_API_requests import report_save, show_all
from .keyboard_services import status_keyboard, tag_keyboard

load_dotenv()

token = os.getenv('bot_token')
rs_chat = int(os.getenv('bot_chat'))
second_chat = int(os.getenv('second_bot_chat'))
refund_chat = int(os.getenv('refund_bot_chat'))
admin_id = int(os.getenv('admin_telegram'))

allowed_chats = [rs_chat, second_chat, refund_chat]
allowed_users = [int(i) for i in os.getenv('allowed_users').split(',')]

bot = telebot.TeleBot(token)


def group_access_check(message):
    """Access to function only from certain chat"""
    return message.chat.id in allowed_chats


def user_access_check(message):
    """Access to function only from certain user"""
    return message.from_user.id in allowed_users


def admin_access_check(message):
    """Access to function only from admin user"""
    return message.from_user.id == admin_id


def check_func(message, urls, keyboard=None, filtered=None):
    """Shows cases depends on the bot command"""
    current_url = urls[message.text]
    if filtered:
        sent = bot.send_message(
            message.from_user.id,
            'Какие кейсы показать?',
            reply_markup=keyboard
        )
        bot.register_next_step_handler(
            sent, show_all, bot, current_url, filtered=filtered
        )
    else:
        show_all(message, bot, current_url)


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
        '/status - фильтр по статусам\n'
        '/status_mn - фильтр по статусам MN\n'
        '/tags - фильтр по тэгам\n'
        '/tags_mn - фильтр по тэгам MN',
        parse_mode='HTML',
    )


@bot.message_handler(func=user_access_check, commands=['rs_all', 'mn_all'])
def check_opened(message):
    """Shows all opened reports"""
    urls = {
        '/rs_all': 'reports',
        '/mn_all': 'mn-reports'
    }
    check_func(message, urls)


@bot.message_handler(func=user_access_check, commands=['status', 'status_mn'])
def check_status(message):
    """Shows reports filtered by status"""
    urls = {
        '/status': 'reports',
        '/status_mn': 'mn-reports'
    }
    check_func(message, urls, keyboard=status_keyboard(), filtered='status')


@bot.message_handler(func=user_access_check, commands=['tags', 'tags_mn'])
def check_tags(message):
    """Shows reports filtered by tag"""
    urls = {
        '/tags': 'reports',
        '/tags_mn': 'mn-reports'
    }
    check_func(message, urls, keyboard=tag_keyboard(), filtered='tag')


@bot.message_handler(func=group_access_check, content_types=['text'])
def post_report(message):
    """Save new report"""
    urls = {
        f'{rs_chat}': 'reports',
        f'{second_chat}': 'mn-reports',
        f'{refund_chat}': 'moneybacks',
    }
    current_chat = str(message.chat.id)
    current_url = urls[current_chat]
    report_save(message, bot, current_url)
