#!/usr/bin/python3
# test_square.py
"""A module for unittesting the Square class"""

import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstance(unittest.TestCase):
    """Class for testing Square inheriting from rectangle intances"""
    def test_square_sub_rectangle(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_intance(self):
        sq = Square(1)

        self.assertIsInstance(sq, Square)

    def test_inherite_attributes_width_height_is_size(self):
        sq = Square(5, 1, 2, 5)

        self.assertEqual(sq.size, 5)

    def test_validate_x(self):
        with self.assertRaises(ValueError) as e:
            sq = Square(5, -1, 2, 5)
            self.assertEqual(e, 'x must be > 0')

    def test_validate_y(self):
        with self.assertRaises(ValueError) as e:
            sq = Square(5, 1, -2, 5)
            self.assertEqual(e, 'y must be > 0')

    def test_validate_y_x(self):
        with self.assertRaises(TypeError) as e:
            sq = Square(5, 1, 0.5, 5)
            self.assertEqual(e, 'x must be an integer')

    def test_validate_size(self):
        with self.assertRaises(TypeError) as e:
            sq = Square('5', 1, 0, 5)
            self.assertEqual(e, 'width must be an integer')

    def test_square_str_overload(self):
        sq = Square(5, 3, 3, 20)

        self.assertEqual(str(sq), '[Square] (20) 3/3 - 5')


class TestSquareUpdate(unittest.TestCase):
    """Class for testing Square public method update that assigns attributes
        with *args and *kwargs

        *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute

            **kwargs can be thought of as a double pointer to a dictionary:
                key/value (keyworded arguments)
            **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
    """

    def test_one_arg(self):
        sq = Square(5)
        sq.update(7)

        self.assertEqual(str(sq), '[Square] (7) 0/0 - 5')

    def test_three_args(self):
        sq = Square(5)
        sq.update(7, 4, 1)

        self.assertEqual(str(sq), '[Square] (7) 1/0 - 4')

    def test_two_kwarg(self):
        sq = Square(5)
        sq.update(x=12, id=6)

        self.assertEqual(str(sq), '[Square] (6) 12/0 - 5')

    def test_three_kwarg(self):
        sq = Square(5)
        sq.update(size=7, id=89, y=1)

        self.assertEqual(str(sq), '[Square] (89) 0/1 - 7')

    def test_all_args(self):
        sq = Square(5)
        sq.update(1, 2, 3, 4)

        self.assertEqual(str(sq), '[Square] (1) 3/4 - 2')

    def test_all_kwargs(self):
        sq = Square(5)
        sq.update(y=0, x=9, size=10, id=45)

        self.assertEqual(str(sq), '[Square] (45) 9/0 - 10')


class TestSquareToDictionary(unittest.TestCase):
    """class for testing the Square public method to_dictionary
        that returns the dictionary representation of a Square

        dictionary contains:
        -id
        -size
        -x
        -y
    """
    def test_type_instance_dict(self):
        sq = Square(10, 2, 1)
        sq_dict = sq.to_dictionary()

        self.assertTrue(type(sq_dict), dict)

    def test_to_dict_output(self):
        sq = Square(10, 2, 1, 11)
        sq_dict = sq.to_dictionary()

        self.assertEqual(
                str(sq_dict), "{'id': 11, 'size': 10, 'x': 2, 'y': 1}")

    def test_to_dict_with_update(self):
        sq = Square(5)
        sq2 = Square(10, 2, 1, 11)
        sq.update(**sq2.to_dictionary())

        self.assertIsInstance(sq, Square)

    def test_to_dict_with_update_output(self):
        sq = Square(5)
        sq2 = Square(10, 2, 1, 11)
        sq.update(**sq2.to_dictionary())

        self.assertEqual(str(sq), '[Square] (11) 2/1 - 10')


if __name__ == '__main__':
    unittest.main()
