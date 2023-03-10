#!/usr/bin/python3
import sys


def add():
    i = 0
    result = 0
    _len = len(sys.argv) - 1
    if _len == 0:
        print("{:d}".format(_len))
    elif _len == 1:
        print("{:d}".format(int(sys.argv[1])))
    else:
        for args in sys.argv:
            if i != 0:
                result += int(args)
            i += 1
        print("{:d}".format(result))


if __name__ == "__main__":
    add()
