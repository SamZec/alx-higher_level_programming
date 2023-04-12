#!/usr/bin/python3
# 3-to_json_string.py
"""A module for to_json_string function that represent object in JSON"""

import json


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object (string)

        my_obj: the object(string) to serialize
    """
    return json.dumps(my_obj)
