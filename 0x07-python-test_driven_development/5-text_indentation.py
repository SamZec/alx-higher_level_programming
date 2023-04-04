#!/usr/bin/python3
# 5-text_indentation.py
"""Text indentation"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of
    these characters: '.', '?' and ':'

    text: the string to be indented

    """
    _str = ''

    if (not isinstance(text, str) or isinstance(text, float) or
            isinstance(text, int) or isinstance(text, bool)):
        raise TypeError('text must be a string')

    for i in text:
        if i == ':' or i == '?' or i == '.':
            _str += i
            _str += '_'
            continue
        _str += i

    str_split = _str.split('_')

    for i in str_split:
        print(i.strip(), end='')
        if i != (str_split[-1]):
            print('\n')
