#!/usr/bin/python3
# 101-add_attribute.py
"""A module that cotains attributes fuction"""


def add_attribute(inst, arg1, arg2):
    """ a function that adds a new attribute to an object if it’s possible

        inst: the object to set attributes to
        areg1: 1st attributes
        arg2: 2nd attributes
    """
    if not hasattr(inst, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(inst, arg1, arg2)
