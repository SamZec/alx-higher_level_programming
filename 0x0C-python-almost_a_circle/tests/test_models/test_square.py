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

        self.assertIsInstance(Square(1), Square)

    def test_square_intance_two_args(self):

        self.assertIsInstance(Square(1, 2), Square)

    def test_square_intance_three_args(self):

        self.assertIsInstance(Square(1, 2, 3), Square)

    def test_inherite_attributes_width_height_is_size(self):
        sq = Square(5, 1, 2, 5)

        self.assertEqual(sq.size, 5)


class TestSquareValidation(unittest.TestCase):
    """class for testing validity of Square attributes"""
    def test_str_size(self):
        with self.assertRaises(TypeError):
            Square('1')

    def test_str_x(self):
        with self.assertRaises(TypeError):
            Square(1, '2')

    def test_str_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, '3')

    def test_validate_x(self):
        with self.assertRaises(ValueError) as e:
            sq = Square(5, -1, 2, 5)
            self.assertEqual(e, 'x must be > 0')

    def test_all_valid_attr(self):

        self.assertIsInstance(Square(1, 2, 3, 4), Square)

    def test_str_size_under_0(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_validate_y(self):
        with self.assertRaises(ValueError) as e:
            Square(1, -2)

    def test_validate_y_x(self):
        with self.assertRaises(ValueError) as e:
            Square(1, 2, -3)

    def test_validate_size(self):
        with self.assertRaises(TypeError) as e:
            sq = Square(0.5, 1, 0, 5)
            self.assertEqual(e, 'width must be an integer')
    def test_str_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_str_overload(self):

        self.assertTrue(Square(5, 3, 3, 20).__str__())


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
    def test_square_update(self):

        self.assertTrue(str(Square(1, 2, 3, 4).update()))

    def test_one_arg(self):
        sq = Square(5)
        sq.update(7)

        self.assertEqual(str(sq), '[Square] (7) 0/0 - 5')

    def test_three_args(self):
        sq = Square(5)
        sq.update(7, 4, 1)

        self.assertEqual(str(sq), '[Square] (7) 1/0 - 4')
    def test_two_args(self):
        sq = Square(5)
        sq.update(7, 4)

        self.assertEqual(str(sq), '[Square] (7) 0/0 - 4')

    def test_two_kwarg(self):
        sq = Square(5)
        sq.update(x=12, id=6)

        self.assertEqual(str(sq), '[Square] (6) 12/0 - 5')

    def test_one_kwarg(self):
        sq = Square(5)
        sq.update(id=6)

        self.assertEqual(str(sq), '[Square] (6) 0/0 - 5')

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

        self.assertTrue(type(Square(1, 2, 3, 4).to_dictionary), dict)

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


class TestSquareCreate(unittest.TestCase):
    """class for testing square update"""
    def test_one_kwarg(self):
        Square.create(**{ 'id': 89 })

    def test_two_kwarg(self):
        Square.create(**{ 'id': 89, 'size': 1 })

    def test_three_kwarg(self):
        Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })

    def test_four_kwarg(self):
        Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })


class TestSquareSaveToFile(unittest.TestCase):
    """class for testing Square inherited save_To_file method"""
    def test_save_to_file_none(self):
        Square.save_to_file(None)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])

    def test_save_to_file(self):
        Square.save_to_file([Square(1)])


if __name__ == '__main__':
    unittest.main()
