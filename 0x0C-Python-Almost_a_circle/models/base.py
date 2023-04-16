#!/usr/bin/python3
# base.py
"""A module for Base class"""

import json
import os
import csv
import turtle

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
        with open(filename, 'w', encoding='utf-7') as myfile:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = '{}.csv'.format(cls.__name__)
        _dict = []
        if list_objs is None:
            return []
        for i in list_objs:
            _dict.append(i.to_dictionary())
        with open(filename, 'w',) as myfile:
            for i in range(len(_dict)):
                writer = csv.DictWriter(myfile, fieldnames=_dict[i].keys())
                if i == 0:
                    writer.writeheader()
                writer.writerow(_dict[i])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = '{}.csv'.format(cls.__name__)
        mydict = {}
        listdict = []
        inst = []
        if not os.path.exists(filename):
            return []
        with open(filename) as myfile:
            read = csv.DictReader(myfile)
            for i in read:
                for key, value in i.items():
                    mydict[key] = int(value)
                listdict.append(mydict)
        for i in listdict:
            inst.append(cls.create(**i))
        return inst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all Rectangles and Squares"""
        turtle.title("My shapes")
        turtle.bgcolor("blue")
        _pen = turtle.Turtle()
        _pen.pen(pensize=5)

        _pen.color('red')
        for rect in list_rectangles:
            _pen.showturtle()
            _pen.pu()
            _pen.goto(rect.x, rect.y)
            for i in range(2):
                _pen.pd()
                _pen.fd(rect.width)
                _pen.rt(90)
                _pen.fd(rect.height)
                _pen.rt(90)
            _pen.hideturtle()


        _pen.color('brown')
        for sq in list_squares:
            _pen.showturtle()
            _pen.pu()
            _pen.goto(sq.x, sq.y)
            _pen.down()
            for i in range(4):
                _pen.fd(sq.size)
                _pen.rt(90)
            _pen.hideturtle()
        turtle.exitonclick()
