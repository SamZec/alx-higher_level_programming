#!/usr/bin/python3
import math


"""MagicClass Object"""


class MagicClass:
    """Creates magic classes"""

    def __init__(self, radius):
        """Intantiate an intance"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Return the area of the object"""

        return (self.__radius**2) * math.pi

    def circumference(self):
        """Return the circumfrence of the object"""

        return 2 * math.pi * self.__radius
