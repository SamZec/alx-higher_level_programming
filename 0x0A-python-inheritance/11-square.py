#!/usr/bin/python3
# 11-square.py
"""A module that contains class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle (9-rectangle.py).
    """
    def __init__(self, size):
        """Intantiation od attributes"""
        self.__size = size
        super().integer_validator('size', self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns the square area"""
        return super().area()

    def __str__(self):
        """returns the name and value of the object"""
        return '[{}] {}/{}'.format(
                type(self).__name__, self.__size, self.__size)
