#!/usr/bin/python3
# 4-inherits_from.py
"""A module containing inherits_from function"""


def inherits_from(obj, a_class):
    """ a function that returns True if the object is an instance
        of a class that inherited (directly or indirectly) from the
        specified class ; otherwise False.
    """
    if isinstance(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
