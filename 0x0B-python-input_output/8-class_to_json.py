#!/usr/bin/python3
# 8-class_to_json.py
"""A module for class_to_json that return dictionary description of class"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for JSON
        serialization of an object

        obj: class instance
    """
    return (obj.__dict__)
