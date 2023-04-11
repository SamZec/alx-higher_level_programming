#!/usr/bin/python3
# 9-rectangle.py
"""A module that contains class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """Intantiation of attributes"""
        self.__width = width
        self.__height = height
        super().integer_validator('width', self.__width)
        super().integer_validator('height', self.__height)

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """return the valuse of width and height"""
        return "[{}] {}/{}".format(
                type(self).__name__, self.__width, self.__height)
