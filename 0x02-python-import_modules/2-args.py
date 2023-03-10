#!/usr/bin/python3
import sys


len_argv = len(sys.argv)
if len_argv <= 1:
    print("0 arguments")
elif len_argv == 2:
    len_argv -= 1
    print("{:d} argument:".format(len_argv))
    print("{:d}: {}".format((len_argv), sys.argv[1]))
elif len_argv > 2:
    len_argv -= 1
    print("{:d} arguments:".format(len_argv))
    len_argv1 = 1
    while len_argv1 <= len_argv:
        print("{:d}: {}".format(len_argv1, sys.argv[len_argv1]))
        len_argv1 += 1
