#!/usr/bin/python3
# 101-locked_class.py
"""Class object"""


class LockedClass:
    """Preventing dynamic attributes creation"""
    __slots__ = ["first_name"]
