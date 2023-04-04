#!/usr/bin/python3
# 0-add_integer.py
"""
a module for addition of integers funtion

"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.
        a: first agument integer or float
        b: second argument integer or float

        Return: integer for a + b
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
