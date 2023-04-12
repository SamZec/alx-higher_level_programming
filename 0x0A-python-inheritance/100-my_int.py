#!/usr/bin/python3
# 100-my_int.py
"""A module containing class MyInt"""


class MyInt(int):
    """a class MyInt that inherits from int"""

    def __eq__(self, other):
        """checks if an object is equal to MyInt"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """checks if an object is not equal to MyInt"""
        return not super().__ne__(other)
