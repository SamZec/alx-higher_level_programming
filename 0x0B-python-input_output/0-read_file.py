#!/usr/bin/python3
# 0-read_file.py
"""A module for read_file function for reading file in UTF-8"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout.

        filename: name of file to read from.
    """
    with open(filename, mode='r', encoding='utf-8') as myfile:
        print(myfile.read(), end='')
