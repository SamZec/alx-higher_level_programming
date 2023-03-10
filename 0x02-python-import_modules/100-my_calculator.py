#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calcus():
    _len = len(sys.argv) - 1
    if _len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, add(a, b)))
    elif sys.argv[2] == '-':
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, sub(a, b)))
    elif sys.argv[2] == '*':
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, mul(a, b)))
    elif sys.argv[2] == '/':
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    calcus()
