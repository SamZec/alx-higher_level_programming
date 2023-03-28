#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Defines square attributes"""

    __size = None

    def __init__(self, size=0):
        "Intantiation of attribute"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
