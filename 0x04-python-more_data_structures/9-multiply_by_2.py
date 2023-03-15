#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        pass

    _dict = dict()
    for i in a_dictionary:
        _dict[i] =  a_dictionary[i] * 2
    return _dict
