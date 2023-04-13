#!/usr/bin/python3
# 10-student.py
"""A module for class student that defines a student"""


class Student:
    """a class Student that defines a student by:

        first_name: first name
        last_name: last name
        age: age in years
    """
    def __init__(self, first_name, last_name, age):
        """Intantiation of attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list and all(isinstance(i, str) for i in attrs):
            return {_k: getattr(self, _k) for _k in attrs if hasattr(self, _k)}
        return self.__dict__
