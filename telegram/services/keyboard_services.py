from telebot import types


def status_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    new = types.KeyboardButton('New')
    actual = types.KeyboardButton('Actual')
    closed = types.KeyboardButton('Closed')
    keyboard.add(
        new, actual, closed
    )
    return keyboard


def tag_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    normal = types.KeyboardButton('Normal')
    burning = types.KeyboardButton('Burning')
    delayed = types.KeyboardButton('Delayed')
    forgotten = types.KeyboardButton('Forgotten')
    keyboard.add(
        normal, burning, delayed, forgotten
    )
    return keyboard
