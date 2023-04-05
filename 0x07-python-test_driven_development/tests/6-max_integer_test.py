#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_result(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4.3, 2.9, 5.5, 2.3]), 5.5)
        self.assertEqual(max_integer([-4, -2, -5, -3, -1]), -1)
        self.assertEqual(max_integer([2000, -4, 500, 300, 100]), 2000)
        self.assertEqual(max_integer([-4]), -4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
