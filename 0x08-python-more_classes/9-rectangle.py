#!/usr/bin/python3
# 8-rectangle.py
"""Rectangle Object"""


class Rectangle:
    """Defines a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize Rectangle instance.

            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1 >= rect_2:
            return rect_1
        if rect_1 < rect_2:
            return rect_2

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
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for k in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return (''.join(rect))

    def __repr__(self):
        """Return rectangle instance"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Delete rectangle instance"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def __ge__(self, other):
        """ returns True based on the area greater-than or equal-to"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """"returns True based on the area less-than"""
        return self.area() < other.area()

    @classmethod
    def square(cls, size=0):
        """Retrun rectangle instance with width == height == size"""
        return cls(size, size)
