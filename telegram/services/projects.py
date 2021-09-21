import requests

from .format_functions import (format_to_save, format_result,
                               format_moneyback_to_save)


class Project:
    """Project class referring to unique DB table"""

    def __init__(self, api_config, chat, endpoint):
        self.api_config = api_config
        self.chat = chat
        self.endpoint = endpoint

    def save(self, *args, **kwargs):
        """Saves project report to DB"""
        to_save = format_to_save(kwargs.get('message'))
        url = (f'http://{self.api_config["host"]}:'
               f'{self.api_config["port"]}/api/v1/{self.endpoint}/')
        headers = {
            'Authorization': f'Token {self.api_config["token"]}',
        }
        try:
            request = requests.post(
                url=url,
                headers=headers,
                json=to_save,
            )
            if request.status_code == 201:
                return 'Отчет успешно записался'
            elif request.status_code == 401:
                return 'Ошибка авторизации, проверьте токен'
            elif request.status_code == 400:
                return f'Отправлены неверные данные: {to_save}'
        except requests.exceptions.ConnectionError:
            return 'Ошибка соединения с сервером'

    def show(self, *args, **kwargs):
        """Shows reports in bot message"""
        root_url = (f'http://{self.api_config["host"]}:'
                    f'{self.api_config["port"]}/api/v1/{self.endpoint}/')
        headers = {
            'Authorization': f'Token {self.api_config["token"]}',
        }
        if 'filter_type' in kwargs:
            report_status = str(kwargs.get('message').text).split()[1]
            filter_url = f'?{kwargs.get("filter_type")}={report_status}'
            url = root_url + filter_url
        else:
            url = root_url
        try:
            reports = requests.get(
                url=url,
                headers=headers
            )
            if reports.status_code == 200:
                output = format_result(reports.json())
                return output
            elif reports.status_code == 401:
                return 'Ошибка авторизации, проверьте токен'
        except requests.exceptions.ConnectionError:
            return 'Ошибка соединения с сервером'


class MoneybackProject(Project):
    """Project moneyback class referring to unique DB table"""

    def save(self, *args, **kwargs):
        """Saves moneyback report to DB"""
        to_save = [format_moneyback_to_save(kwargs.get('message'))]
        super().save(*args, **kwargs)
