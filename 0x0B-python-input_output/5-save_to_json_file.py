#!/usr/bin/python3
# 5-save_to_json_file.py
"""A module for save_to_json_file function for writing obj to file by JSON"""

import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
            using a JSON representation.

        my_obj: object to write into file
        filename: file to write object into
    """
    with open(filename, mode='w', encoding='UTF-8') as myfile:
        json.dump(my_obj, myfile, sort_keys=True)
