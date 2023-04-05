#!/usr/bin/python3
# 3-say_my_name.py
"""
    A module that prints names

"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name is <first name> <last name>

    first_name: takes first name string
    last_name: takes last name string or defaut to empty string

    prints: My name is <first name> <last name>

    """
    if ((not isinstance(first_name, str) and first_name is None)
            or first_name == ''):
        raise TypeError('first_name must be a string')
    if isinstance(first_name, int) or isinstance(first_name, float):
        raise TypeError('first_name must be a string')
    if isinstance(last_name, int) or isinstance(last_name, float):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
