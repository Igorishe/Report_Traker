from .parse_functions import parse_report


tags_emoji = {
    'Normal': '\ud83c\udd97 ',
    'Burning': '\ud83d\udd25 ',
    'Delayed': '\ud83d\udd57 ',
    'Forgotten': '\ud83d\ude31 '
}

status_emoji = {
    'New': '\ud83d\udce9 ',
    'Actual': '\ud83d\udcd6 ',
    'Closed': '\ud83d\udd12 ',
}


def decode_surrogates(string):
    return string.encode(
            'utf-16', 'surrogatepass').decode('utf-16', 'surrogatepass')


def format_result(result):
    """Format API response for telegram rendering"""
    output = ''
    for item in result:
        text = item['text']
        date = item['date']
        response_status = item['status']
        emoji = decode_surrogates(status_emoji[response_status])
        status = emoji + response_status
        response_tag = item['tag']
        emoji = decode_surrogates(tags_emoji[response_tag])
        tag = emoji + response_tag
        author = item['author_name']
        line = (
            f'Кейс: {text}\n'
            f'<code>Дата: {date}</code>\n'
            f'Статус: <b>{status}</b>\n'
            f'Тэг: <b>{tag}</b>\n'
            f'Автор: @{author}\n'
            '____________________________________\n'
        )
        output += line
    if not output:
        return 'Эта категория пуста'
    if len(output) > 4096:
        return output[:4096]
    return output


def format_to_save(message):
    """Serialize report objects for POST request"""
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
        if report.startswith('!!!'):
            obj_to_save['text'] = report[3:]
            obj_to_save['tag'] = 'Burning'
        to_save.append(obj_to_save)
    return to_save
