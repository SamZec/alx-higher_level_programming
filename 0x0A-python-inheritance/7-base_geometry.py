#!/usr/bin/python3
# 7-base_geometry.py
"""A module containing base_geometry class"""


class BaseGeometry:
    """a class that defines a geometry"""
    def area(self):
        """not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates integer value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
