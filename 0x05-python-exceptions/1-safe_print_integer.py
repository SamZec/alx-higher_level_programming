#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True
