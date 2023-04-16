#!/usr/bin/python3
# square.py
"""A module for class Square that inherit from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Intantiation of attributes

            size: size of square
            x: position on x-axis
            y: position on y-axis
            id: square instance identification
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square instance"""
        return '[{}] ({:d}) {:d}/{:d} - {:d}'.format(
                type(self).__name__, self.id, self.x,
                self.y, self.height)

    def update(self, *args, **kwargs):
        """assigns attributes"""
        attrs = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size
