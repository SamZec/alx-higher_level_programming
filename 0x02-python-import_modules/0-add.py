#!/usr/bin/python3
from add_0 import add


def _add():
    a = 1
    b = 2
    result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))


if __name__ == "__main__":
    _add()
