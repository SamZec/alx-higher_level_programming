#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
def calcus():
    a = 10
    b = 5
    result = add(a, b)
    result1 = sub(a ,b)
    result2 = mul(a, b)
    result3 = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
    print("{:d} - {:d} = {:d}".format(a, b, result1))
    print("{:d} * {:d} = {:d}".format(a, b, result2))
    print("{:d} / {:d} = {:d}".format(a, b, result3))
if __name__ == "__main__":
    calcus()
