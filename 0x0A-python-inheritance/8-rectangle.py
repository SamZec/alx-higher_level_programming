#!/usr/bin/python3
# 8-rectangle.py
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
