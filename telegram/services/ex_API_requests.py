import os

import requests
from dotenv import load_dotenv

from .parse_functions import parse_report

load_dotenv()

jwt_token = os.getenv('jwt_token')
refresh_token = os.getenv('jwt_refresh')


def format_result(result):
    """Format API response for telegram rendering"""
    output = ''
    for item in result:
        text = item['text']
        date = item['date']
        status = item['status']
        author = item['author_name']
        line = (
            f'Кейс: {text}\n'
            f'<code>Дата: {date}</code>\n'
            f'Статус: <b>{status}</b>\n'
            f'Автор: {author}\n'
            '\n'
        )
        output += line
    if not output:
        return 'Эта категория пуста'
    return output


def show_all(message, bot):
    """Get reports list from Traker API"""
    reports_status = str(message.text)
    try:
        reports = requests.get(
            url=f'http://127.0.0.1:8000/api/v1/report/?status={reports_status}',
            headers={
                'Authorization': f'Bearer {jwt_token}',
            }
        )
        if reports.status_code == 200:
            result = reports.json()
            output = format_result(result)
            bot.send_message(
                message.from_user.id,
                output,
                parse_mode='HTML',
            )
        elif reports.status_code == 401:
            bot.send_message(
                message.from_user.id,
                'Ошибка авторизации, проверьте токен',
            )
    except requests.exceptions.ConnectionError:
        bot.send_message(
            message.from_user.id,
            'Ошибка соединения с сервером',
        )


def report_save(message, bot):
    """Post new report to Traker base"""
    text = message.text
    reports = parse_report(text)
    author_id = message.from_user.id
    author_username = message.from_user.username
    to_save = []
    for report in reports:
        obj_to_save = {
            'author': author_id,
            'author_name': author_username,
            'text': report,
        }
        to_save.append(obj_to_save)
    try:
        request = requests.post(
            url='http://127.0.0.1:8000/api/v1/report/',
            headers={
                'Authorization': f'Bearer {jwt_token}',
            },
            json=to_save,
        )
        bot.send_message(
            message.from_user.id,
            request.status_code,
        )
    except requests.exceptions.ConnectionError:
        bot.send_message(
            message.from_user.id,
            'Ошибка соединения с сервером',
        )
