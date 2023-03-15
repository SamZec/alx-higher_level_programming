#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        pass

    for i in a_dictionary:
        a_dictionary[i] *= 2
    return a_dictionary
