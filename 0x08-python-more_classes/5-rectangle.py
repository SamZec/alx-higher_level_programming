#!/usr/bin/python3
# 5-rectangle.py
"""Rectangle Object"""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle instance.

            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Retunrn the perimeter"""
        if self.__height != 0 and self.__width != 0:
            return 2 * (self.__height + self.__width)
        else:
            return 0

    def __str__(self):
        """Return the rectangle shape"""
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for i in range(self.__height):
                rect.append('#' * self.__width)
            return ('\n'.join(rect))

    def __repr__(self):
        """Return rectangle instance"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Delete rectangle instance"""
        print('Bye rectangle...')
