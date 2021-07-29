import os

import telebot
from dotenv import load_dotenv

from .ex_API_requests import show_all, report_save
from .keyboard_services import status_keyboard, tag_keyboard

load_dotenv()

token = os.getenv('bot_token')
chat = int(os.getenv('bot_chat'))
second_chat = int(os.getenv('second_bot_chat'))

allowed_chats = [chat, second_chat]

bot = telebot.TeleBot(token)


def group_access_check(message):
    """Access to function only from certain chat"""
    return message.chat.id in allowed_chats


@bot.message_handler(commands=['group'])
def show_group(message):
    """Shows tg group id"""
    bot.send_message(
        message.chat.id,
        message.chat.id,
    )


@bot.message_handler(commands=['start', 'help'])
def start(message):
    """Greeting message"""
    bot.send_message(
        message.from_user.id,
        '<b>Привет! Все отчеты здесь!</b>\n\n'
        '/status - фильтр по статусам\n'
        '/status_mn - фильтр по статусам MN\n'
        '/tags - фильтр по тэгам\n'
        '/tags_mn - фильтр по тэгам MN',
        parse_mode='HTML',
    )


@bot.message_handler(commands=['status', 'status_mn'])
def check(message):
    """Shows reports filtered by status"""
    urls = {
        '/status': 'report',
        '/status_mn': 'mn-report'
    }
    current_url = urls[message.text]
    sent = bot.send_message(
        message.from_user.id,
        'Какие кейсы показать?',
        reply_markup=status_keyboard()
    )
    bot.register_next_step_handler(sent, show_all, bot, 'status', current_url)


@bot.message_handler(commands=['tags', 'tags_mn'])
def check_tags(message):
    """Shows reports filtered by status"""
    urls = {
        '/tags': 'report',
        '/tags_mn': 'mn-report'
    }
    current_url = urls[message.text]
    sent = bot.send_message(
        message.from_user.id,
        'Какие кейсы показать?',
        reply_markup=tag_keyboard()
    )
    bot.register_next_step_handler(sent, show_all, bot, 'tag', current_url)


@bot.message_handler(func=group_access_check, content_types=['text'])
def post_report(message):
    """Save new report"""
    urls = {
        f'{chat}': 'report',
        f'{second_chat}': 'mn-report',
    }
    current_chat = str(message.chat.id)
    current_url = urls[current_chat]
    report_save(message, bot, current_url)
