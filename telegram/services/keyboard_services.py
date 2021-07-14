from telebot import types


def status_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    normal = types.KeyboardButton('Normal')
    urgent = types.KeyboardButton('Urgent')
    closed = types.KeyboardButton('Closed')
    forgotten = types.KeyboardButton('Forgotten')
    keyboard.add(
        normal, urgent, closed, forgotten
    )
    return keyboard
