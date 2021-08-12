import os

import requests
from dotenv import load_dotenv

from .format_functions import format_result, format_to_save

load_dotenv()

admin_id = int(os.getenv('admin_telegram'))
api_token = os.getenv('api_token')
api_host = os.getenv('api_host')
api_port = '8000'


def show_all(message, bot, current_url, filtered=None):
    """Get reports list from Traker API"""
    root_url = f'http://{api_host}:{api_port}/api/v1/{current_url}/'
    if filtered:
        report_status = str(message.text)
        filter_url = f'?{filtered}={report_status}'
        url = root_url + filter_url
    else:
        url = root_url
    try:
        reports = requests.get(
            url=url,
            headers={
                'Authorization': f'Token {api_token}',
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


def report_save(message, bot, current_url):
    """Post new report to Traker base"""
    to_save = format_to_save(message)
    try:
        request = requests.post(
            url=f'http://{api_host}:{api_port}/api/v1/{current_url}/',
            headers={
                'Authorization': f'Token {api_token}',
            },
            json=to_save,
        )
        if request.status_code == 201:
            bot.send_message(
                admin_id,
                'Отчет успешно записался',
            )
        elif request.status_code == 401:
            bot.send_message(
                admin_id,
                'Ошибка авторизации, проверьте токен',
            )
    except requests.exceptions.ConnectionError:
        bot.send_message(
            admin_id,
            'Ошибка соединения с сервером',
        )
