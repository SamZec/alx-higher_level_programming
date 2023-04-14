#!/usr/bin/python3
# base.py
"""A module for Base class"""


class Base:
    """the “base” of all other classes in my project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Intatiation of attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
