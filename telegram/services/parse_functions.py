import re


def parse_report(text):
    """Split report to single cases"""
    regexp = r'\d\.\s'
    result_split = re.split(regexp, text)
    result_none = list(filter(None, result_split))
    result = [element.rstrip().rstrip(';') for element in result_none]
    return result


def parse_moneyback(text):
    """Split moneyback report to single fields"""
    result = {}
    field_names = {
        'wallet': 'Кошелек',
        'value': 'Сумма',
        'link': 'Ссылка',
        'text': 'Описание',
        'payment_system': 'Система',
    }
    array = text.split('\n\n')
    for name in field_names.items():
        key, value = name
        raw_field = list(filter(lambda x: x.startswith(value), array))[0]
        field = raw_field.replace(f'{value}: ', '')
        result[key] = field
    return result
