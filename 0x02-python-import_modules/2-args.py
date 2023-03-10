#!/usr/bin/python3
import sys


def _args():
    len_argv = len(sys.argv) - 1
    if len_argv == 0:
        print("{:d} arguments".format(len_argv))
    elif len_argv == 1:
        print("{:d} argument:".format(len_argv))
        print("{:d}: {}".format((len_argv), sys.argv[1]))
    else:
        print("{:d} arguments:".format(len_argv))
        len_argv1 = 1
        while len_argv1 <= len_argv:
            print("{:d}: {}".format(len_argv1, sys.argv[len_argv1]))
            len_argv1 += 1


if __name__ == "__main__":
    _args()
