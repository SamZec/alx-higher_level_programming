#!/usr/bin/python3
# rectangle.py
"""A module for Rectangle class that inherit from Base"""

from base import Base


class Rectangle(Base):
    """A class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Intantiation of attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """returns the area value of a Rectangle instance."""
        return self.__height * self.__width

    def display(self):
        """prints the Rectangle instance with the character #"""
        [print("") for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end='') for i in range(self.__x)]
            [print('#', end='') for i in range(self.__width)]
            print()

    def __str__(self):
        return '[{}] ({}) {}/{} - {}/{}'.format(
                Rectangle.__name__, self.id, self.__x,
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attributes"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width validation"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    def to_dictionary(self):
        """dictionary reprensentation of rectangle"""
        return {
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
                }

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height validation"""
        if type(height) is not int:
            raise TypeError('heigth must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x validation"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be > 0')
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y validation"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be > 0')
        self.__y = y
