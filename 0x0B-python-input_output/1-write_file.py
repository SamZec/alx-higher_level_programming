#!/usr/bin/python3
# 1-write_file.py
"""A module for write_file function for writing string to text file"""


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8)
        and returns the number of characters written

        filename: file to write to
        text: string to write to file
    """
    with open(filename, mode='w', encoding='UTF-8') as myfile:
        chs = myfile.write(text)
    return chs
