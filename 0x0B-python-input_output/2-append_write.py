#!/usr/bin/python3
# 2-append_write.py
"""A module for append_write function which appends text string to a file"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added.

        filename: file to append to.
        text: the string to append
    """
    with open(filename, mode='a', encoding='UTF-8') as myfile:
        chs = myfile.write(text)

    return chs
