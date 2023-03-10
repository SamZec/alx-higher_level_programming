#!/usr/bin/python3
import sys


def _args():
    i = 0
    _len = len(sys.argv) - 1
    if _len == 1:
        print("{:d} argument:".format(_len))
    elif _len == 0:
        print("{:d} arguments.".format(_len))
    else:
        print("{:d} arguments:".format(_len))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    _args()
