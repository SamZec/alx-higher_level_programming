#!/usr/bin/python3
# 2-is_same_class.py
"""a mudule that contains is_same_class function"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly
        an instance of the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
