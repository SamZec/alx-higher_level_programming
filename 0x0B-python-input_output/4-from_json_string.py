#!/usr/bin/python3
# 4-from_json_string.py
"""A module for from_json_string function return JSON string to pyhon data"""

import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
            represented by a JSON string

        my_str: JSON string to be deserialized
    """
    return json.loads(my_str)
