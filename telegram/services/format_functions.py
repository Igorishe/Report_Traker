from .parse_functions import parse_report


def format_result(result):
    """Format API response for telegram rendering"""
    output = ''
    for item in result:
        text = item['text']
        date = item['date']
        status = item['status']
        tag = item['tag']
        author = item['author_name']
        line = (
            f'Кейс: {text}\n'
            f'<code>Дата: {date}</code>\n'
            f'Статус: <b>{status}</b>\n'
            f'Тэг: <b>{tag}</b>\n'
            f'Автор: {author}\n'
            '________________________________\n'
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
