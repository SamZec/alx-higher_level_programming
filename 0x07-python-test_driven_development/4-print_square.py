#!/usr/bin/python3
# 4-print_square.py
"""Print square"""


def print_square(size):
    """a function that prints a square with the character #.
        size: the length of square (integer or float) > 0
    """
    if ((not isinstance(size, int) and not isinstance(size, float)) or
            isinstance(size, bool)):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    _size = int(size)
    if _size < 0:
        raise ValueError('size must be >= 0')
    for i in range(_size):
        print('#' * _size)
