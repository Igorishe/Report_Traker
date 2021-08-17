from telebot import types

from .format_functions import status_emoji, tags_emoji


def status_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    new = types.KeyboardButton(status_emoji['New'] + 'New')
    actual = types.KeyboardButton(status_emoji['Actual'] + 'Actual')
    closed = types.KeyboardButton(status_emoji['Closed'] + 'Closed')
    keyboard.add(
        new, actual, closed
    )
    return keyboard


def tag_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    normal = types.KeyboardButton(tags_emoji['Normal'] + 'Normal')
    burning = types.KeyboardButton(tags_emoji['Burning'] + 'Burning')
    delayed = types.KeyboardButton(tags_emoji['Delayed'] + 'Delayed')
    forgotten = types.KeyboardButton(tags_emoji['Forgotten'] + 'Forgotten')
    keyboard.add(
        normal, burning, delayed, forgotten
    )
    return keyboard
