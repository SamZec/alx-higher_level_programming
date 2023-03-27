#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as e:
        print("Exeception: {}".format(e), file=stderr)
        return result
    else:
        return result
