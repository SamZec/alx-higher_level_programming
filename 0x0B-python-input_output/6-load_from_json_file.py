#!/usr/bin/python3
# 6-load_from_json_file.py
"""A module for load_from_json_file function that creates object from JSON"""

import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”

        filename: file to write object to
    """
    with open(filename, encoding='UTF-8') as myfile:
        return json.load(myfile)
