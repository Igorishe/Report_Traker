import re


def parse_report(text):
    """Split report to single cases"""
    regexp = r'\d\.\s'
    result_split = re.split(regexp, text)
    result_none = list(filter(None, result_split))
    result = [element.rstrip().rstrip(';') for element in result_none]
    return result
