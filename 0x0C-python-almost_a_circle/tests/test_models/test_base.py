#!/usr/bin/python3
# test_base.py
"""A test case module for class Base"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstance(unittest.TestCase):
    """class to test Base instances"""
    def test_base_type(self):
        self.assertEqual(Base.__name__, 'Base')

    def test_no_args(self):
        b1 = Base()
        b2 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertNotEqual(b1.id, b2.id)

    def test_args_int(self):
        b3 = Base(5)

        self.assertEqual(b3.id, 5)

    def test_args_string(self):
        b4 = Base("Hi")

        self.assertEqual(b4.id, 'Hi')

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, "Hi")

    def test_public_id(self):
        b5 = Base()
        b5.id = 20

        self.assertEqual(b5.id, 20)

    def test_private_attribute(self):
        with self.assertRaises(AttributeError):
            Base(25).__nb_objects


class Test_from_json_string(unittest.TestCase):
    """class for testing json string represnetation from dict"""
    def test_rect_dict(self):
        rect = Rectangle(1, 7, 9, 2, 3)

        self.assertEqual(str, type(Base.to_json_string(rect.to_dictionary())))

    def test_rect_list_dict(self):
        list_dict = [Rectangle(1, 7, 9, 2, 3).to_dictionary()]
        list_dict.append(Rectangle(1, 7, 9, 2, 3).to_dictionary())

        self.assertEqual(str, type(Base.to_json_string(list_dict)))

    def test_none_or_empty_rect_dict(self):
        list_dict = []

        self.assertEqual(str, type(Base.to_json_string(None)))
        self.assertTrue(len(Base.to_json_string(list_dict)) == len('[]'))

    def test_sq_dict(self):
        sq = Square(7, 9, 2, 3)

        self.assertEqual(str, type(Base.to_json_string(sq.to_dictionary())))

    def test_sq_list_dict(self):
        list_dict = [Square(1, 9, 2, 3).to_dictionary()]
        list_dict.append(Square(1, 9, 2, 3).to_dictionary())

        self.assertEqual(str, type(Base.to_json_string(list_dict)))

    def test_none_or_empty_sq_dict(self):
        list_dict = []

        self.assertEqual(str, type(Base.to_json_string(None)))
        self.assertTrue(len(Base.to_json_string(list_dict)) == len('[]'))


class TestSaveToFile(unittest.TestCase):
    """class to test the method save_to_file that writes to file"""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_none_arg(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file(l=[], ls=[])

    def test_not_int_arg(self):
        Rectangle.save_to_file(1)
        with open('Rectangle.json') as f:
            self.assertEqual(f.read(), '[]')

    def test_not_tupple_arg(self):
        Square.save_to_file(("h", "y"))
        with open('Square.json') as f:
            self.assertEqual(f.read(), '[]')

    def test_NaN_arg(self):
        Rectangle.save_to_file(float('NAN'))
        with open('Rectangle.json') as f:
            self.assertEqual(f.read(), '[]')

    def test_not_tupple_arg(self):
        Square.save_to_file(float('INF'))
        with open('Square.json') as f:
            self.assertEqual(f.read(), '[]')

    def test_rect_inst(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            self.assertEqual(type(f.read()), str)

    def test_sq_inst(self):
        sq1 = Square(20)
        sq2 = Square(30)
        Square.save_to_file([sq1, sq2])

        with open('Square.json') as f:
            self.assertEqual(type(f.read()), str)


class TestDictionaryToInstance(unittest.TestCase):
    """class for testing create method that returns instance from dict"""
    def test_rect_dict_to_instance(self):
        rect = Rectangle(25, 7, 9)
        rect_dict = rect.to_dictionary()
        rect2 = Rectangle.create(**rect_dict)

        self.assertIsInstance(rect2, Rectangle)
        self.assertNotEqual(rect, rect2)

    def test_rect_create_no_args(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()
            rect.create()

    def test_rect_create_no_args(self):
        with self.assertRaises(TypeError):
            _dict = dict
            Rectangle.create(_dict)

    def test_sq_dict_to_instance(self):
        sq = Square(25, 7, 9)
        sq_dict = sq.to_dictionary()
        sq2 = Square.create(**sq_dict)

        self.assertIsInstance(sq2, Square)
        self.assertNotEqual(sq, sq2)

    def test_sq_create_no_args(self):
        with self.assertRaises(TypeError):
            sq = Square()
            sq.create()

    def test_sq_create_no_pointer(self):
        with self.assertRaises(TypeError):
            _dict = {}
            Square.create(_dict)


class TestFileToInstances(unittest.TestCase):
    """class for testing load_from_file that returns a list of instances"""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_rect_1_instance_from_file(self):
        rect1 = Rectangle(7, 8, 0, 2, 30)
        Rectangle.save_to_file([rect1])
        rect2 = Rectangle.load_from_file()

        self.assertEqual(str(rect1), '[Rectangle] (30) 0/2 - 7/8')

    def test_rect_2_instance_from_file(self):
        rect1 = Rectangle(7, 8, 0, 2, 30)
        rect2 = Rectangle(7, 8, 0, 2, 45)
        Rectangle.save_to_file([rect1, rect2])
        list_rect = Rectangle.load_from_file()

        self.assertEqual(str(rect2), str(list_rect[1]))

    def test_rect_instance_from_file(self):
        rect1 = Rectangle(7, 8, 0, 2, 30)
        Rectangle.save_to_file([rect1])
        list_rect = Rectangle.load_from_file()

        self.assertEqual(type(list_rect[0]), Rectangle)

    def test_sq_1_from_file(self):
        sq = Square(8, 0, 3, 90)
        Square.save_to_file([sq])
        list_sq = Square.load_from_file()

        self.assertEqual(str(sq), '[Square] (90) 0/3 - 8')

    def test_sq_2_from_file(self):
        sq1 = Square(8, 0, 3, 90)
        sq2 = Square(8, 0, 3, 91)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()

        self.assertEqual(str(list_sq[1]), str(sq2))

    def test_sq_instance_from_file(self):
        sq1 = Square(8, 0, 3, 92)
        sq2 = Square(8, 0, 3, 93)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()

        self.assertEqual(type(list_sq[1]), Square)

    def test_load_no_file(self):
        _none = Base.load_from_file()

        self.assertEqual([], _none)

    def test_load_from_file_mul_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(None, None)


class TestBase_save_to_file_csv(unittest.TestCase):
    """class for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_rect1(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_rect2(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_sq1(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])

        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_sq2(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual('[]', f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual('[]', f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_mult_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """class for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_rect1(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_rect2(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rect_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_sq1(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_sq2(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_sq_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual('[]', output)

    def test_load_from_file_csv_mult_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv(None, 1)


if __name__ == '__main__':
    unittest.main()
