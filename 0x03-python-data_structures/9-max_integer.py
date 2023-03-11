#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    _sort = sorted(my_list, reverse=True)
    return _sort[0]
