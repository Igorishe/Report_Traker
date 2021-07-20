import os

import telebot
from dotenv import load_dotenv

from .ex_API_requests import show_all, report_save
from .keyboard_services import status_keyboard, tag_keyboard

load_dotenv()

token = os.getenv('bot_token')
chat = int(os.getenv('bot_chat'))

bot = telebot.TeleBot(token)


def group_access_check(message):
    """Access to function only from certain chat"""
    return message.chat.id == chat


@bot.message_handler(commands=['start', 'help'])
def start(message):
    """Greeting message"""
    bot.send_message(
        message.from_user.id,
        '<b>Привет! Все отчеты здесь!</b>\n\n'
        '/status - фильтр по статусам\n'
        '/tags - фильтр по тэгам',
        parse_mode='HTML',
    )


@bot.message_handler(commands=['status'])
def check(message):
    """Shows reports filtered by status"""
    sent = bot.send_message(
        message.from_user.id,
        'Какие кейсы показать?',
        reply_markup=status_keyboard()
    )
    bot.register_next_step_handler(sent, show_all, bot, 'status')


@bot.message_handler(commands=['tags'])
def check_tags(message):
    """Shows reports filtered by status"""
    sent = bot.send_message(
        message.from_user.id,
        'Какие кейсы показать?',
        reply_markup=tag_keyboard()
    )
    bot.register_next_step_handler(sent, show_all, bot, 'tag')


@bot.message_handler(func=group_access_check, content_types=['text'])
def post_report(message):
    """Save new report"""
    report_save(message, bot)


# bot.polling(none_stop=True)
