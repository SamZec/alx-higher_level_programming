#!/usr/bin/python3
# base.py
"""A module for Base class"""

import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = '{}.json'.format(cls.__name__)
        _dict = []
        if list_objs is not None:
            for i in list_objs:
                _dict.append(i.to_dictionary())
        with open(filename, 'w', encoding='utf-8') as myfile:
            myfile.write(cls.to_json_string(_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            inst = cls(50)
        else:
            inst = cls(50, 50)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = '{}.json'.format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename) as myfile:
            _str = myfile.read()
        _dict = cls.from_json_string(_str)
        inst = []
        for i in _dict:
            inst.append(cls.create(**i))
        return inst
