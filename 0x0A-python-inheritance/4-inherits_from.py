#!/usr/bin/python3
# 4-inherits_from.py
"""A module containing inherits_from function"""


def inherits_from(obj, a_class):
    """ a function that returns True if the object is an instance
        of a class that inherited (directly or indirectly) from the
        specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(a, a_class)
