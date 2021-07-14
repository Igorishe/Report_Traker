import re


def parse_report(text):
    """Split report to single cases"""
    regexp = r'\d\.\s'
    result = re.split(regexp, text)
    result = list(filter(None, result))
    result = [element.rstrip().rstrip(';') for element in result]
    return result
