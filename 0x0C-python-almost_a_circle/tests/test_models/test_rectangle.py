#!/usr/bin/python3
# test_rectangle.py
"""A module for unittesting the the Rectangle class"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstance(unittest.TestCase):
    """Class for testing the creation and instances of Rectangle class"""
    def test_create_rectangle(self):
        self.assertTrue(type(Rectangle), Base)

    def test_instance_rect_two_args(self):

        self.assertIsInstance(Rectangle(10, 20), Rectangle)

    def test_chect_rect_instance_three_args(self):

        self.assertIsInstance(Rectangle(10, 20, 0), Rectangle)

    def test_rect_instance_four_args(self):

        self.assertIsInstance(Rectangle(10, 20, 0, 3), Rectangle)

    def test_check_rect_instance_five_args(self):

        self.assertIsInstance(Rectangle(10, 20, 0, 3, 50), Rectangle)

    def test_rect_None_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1)


class TestValidateRectangle(unittest.TestCase):
    """Class to test Rectanlgle class attributes validation"""
    def Test_str_width(self):
        with self.assertRaises(TypeError):
            Rectangle('1', 2)

    def Test_str_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, '2')

    def Test_str_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, '3')

    def Test_str_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, '4')

    def test_with_0(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 1)

    def test_height_0(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)

    def test_with_under_0(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 2)

    def test_height_under_0(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, -2)

    def test_with_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(0.5, 2)

    def test_with_bool(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(True, 2)

    def test_height_NaN(self):
        with self.assertRaises(TypeError) as e:
            rect = Rectangle(3, float('NAN'))

            self.assertEqual(e, 'height must be an integer')

    def test_height_infinity(self):
        with self.assertRaises(TypeError) as e:
            rect = Rectangle(3, float('INF'))

            self.assertEqual(e, 'height must be an integer')

    def test_0_attribute_width(self):
        with self.assertRaises(ValueError) as e:
            rect = Rectangle(0, 3)

            self.asserEqual(e,  'width must be > 0')

    def test_0_attribute_height(self):
        with self.assertRaises(ValueError) as e:
            rect = Rectangle(3, -9)

            self.asserEqual(e,  'height must be > 0')

    def test_0_attribute_width_height(self):
        with self.assertRaises(ValueError) as e:
            rect = Rectangle(-1, 0)

            self.asserEqual(e,  'width must be > 0')

    def test_under_0_x(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -3)

    def test_under_0_y(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, -4)

    def test_under_0_x_and_y(self):
        with self.assertRaises(TypeError) as e:
            rect = Rectangle(1, 3, 0.2, -5)

            self.asserEqual(e,  'x must be an integer')


class TestRectangleArea(unittest.TestCase):
    """Class for testing Rectangle public method area"""
    def test_area(self):

        self.assertEqual(Rectangle(1, 2).area(), 2)

    def test_area_string(self):
        with self.assertRaises(TypeError) as e:
            rect = Rectangle('5', '5')
            a = rect.area()
            self.assertEqual(e, 'width must be integer')

    def test_area_float(self):
        with self.assertRaises(TypeError) as e:
            rect = Rectangle(0.5, 0.5)
            a = rect.area()
            self.assertEqual(e, 'width must be integer')

    def test_area_unde_0(self):
        with self.assertRaises(ValueError) as e:
            rect = Rectangle(5, -5)
            a = rect.area()
            self.assertEqual(e, 'height must be > 0')


class TestRectangle__str__(unittest.TestCase):
    """
        Class to test the Rectangle method __str__ that return
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
    """

    def test_rect__str__(self):

        self.assertTrue(Rectangle(1, 2).__str__())

    def test_rect_str_ouput_width_height(self):
        rect = Rectangle(10, 10)

        self.assertEqual(
                str(rect), '[Rectangle] ({}) 0/0 - 10/10'.format(rect.id))

    def test_rect_str_ouput_width_height_x(self):
        rect = Rectangle(10, 10, 5)
        self.assertEqual(
                str(rect), '[Rectangle] ({}) 5/0 - 10/10'.format(rect.id))

    def test_rect_str_ouput_width_height_x_y(self):
        rect = Rectangle(10, 10, 6, 9)

        self.assertEqual(
                str(rect), '[Rectangle] ({}) 6/9 - 10/10'.format(rect.id))

    def test_rect_str_ouput_width_height_x_y_id(self):
        rect = Rectangle(10, 10, 3, 4, 27)

        self.assertEqual(
                str(rect), '[Rectangle] (27) 3/4 - 10/10'.format(rect.id))


class TestRectangleDisplay(unittest.TestCase):
    """class for testing the public method display of Rectangle class"""
    def test_display_width_height(self):

        Rectangle(1, 2).display()

    def test_display_width_height_x(self):

        Rectangle(1, 2, 3).display()

    def test_display_width_height_x_y(self):

        Rectangle(1, 2, 3, 4).display()


class TestRectangleUpdate(unittest.TestCase):
    """Class to test rectangle public method update that assigns args to attr

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
    """
    def test_update_id_arg(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)

        self.assertEqual(rect.id, 89)

    def test_update_id_width_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2)

        self.assertEqual(rect.width, 2)

    def test_update_id_width_height_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3)

        self.assertEqual(rect.height, 3)

    def test_update_id_width_height_x_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4)

        self.assertEqual(rect.x, 4)

    def test_update_id_width_height_x_yargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)

        self.assertEqual(rect.y, 5)

    def test_check_update_output(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(100, 2, 3, 2, 8)

        self.assertEqual(str(rect), '[Rectangle] (100) 2/8 - 2/3')


class TestRectangleUpdateArgsKwargs(unittest.TestCase):
    """class to test Rectangle public method update  with
        *args, **kwargs that assigns a key/value argument to attributes
    """
    def test_update_one_key(self):
        rect = Rectangle(1, 1)
        rect.update(height=5)

        self.assertTrue(rect.height, 5)

    def test_update_two_keys(self):
        rect = Rectangle(1, 1)
        rect.update(height=5, x=5)

        self.assertTrue(rect.height, 5)
        self.assertEqual(rect.x, 5)

    def test_update_three_keys(self):
        rect = Rectangle(1, 1)
        rect.update(y=1, width=2, height=5)

        self.assertTrue(rect.height, 5)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.width, 2)

    def test_update_four_keys(self):
        rect = Rectangle(1, 1)
        rect.update(y=1, width=2, height=5, x=9)

        self.assertTrue(rect.height, 5)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.x, 9)

    def test_update_five_keys(self):
        rect = Rectangle(1, 1)
        rect.update(y=1, width=2, id=40, height=5, x=9)

        self.assertTrue(rect.height, 5)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.id, 40)
        self.assertEqual(rect.x, 9)

    def test_update_kwargs_output(self):
        rect = Rectangle(1, 1)
        rect.update(y=1, width=2, id=40, height=5, x=9)

        self.assertEqual(str(rect), '[Rectangle] (40) 9/1 - 2/5')


class TestRectangleCreate(unittest.TestCase):
    """Class to test rectangle method create"""
    def test_one_kwarg(self):
        Rectangle.create(**{'id': 89})

    def test_two_kwargs(self):
        Rectangle.create(**{'id': 89, 'width': 1})

    def test_three_kwargs(self):
        Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})

    def test_four_kwargs(self):
        Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})

    def test_five_kwarg(self):
        Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})


class TestRectangleToDictionary(unittest.TestCase):
    """Class for testing Rectangle public method to_dictionary that dict
        representation of Rectangle

        contains dict keys:
        id
        width
        height
        x
        y
    """
    def test_check_instance_dict(self):
        rect = Rectangle(10, 2, 1, 9)
        rect_dict = rect.to_dictionary()

        self.assertTrue(type(rect_dict), dict)

    def test_print_instance_dict(self):
        rect = Rectangle(10, 2, 1, 9, 1)
        rect_dict = rect.to_dictionary()

        self.assertEqual(
                str(rect_dict),
                "{'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}")


class TestRectangleToFileFromFile(unittest.TestCase):
    """class to test save_to_file and load_from_file methods"""
    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])

    def test_save_to_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])

    def test_load_from_file_no_file(self):
        Rectangle.load_from_file()

    def test_load_from_file_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        Rectangle.load_from_file()


if __name__ == '__name__':
    unitest.main()
