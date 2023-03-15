#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        pass

    _sort = sorted(a_dictionary)
    for i in _sort:
        print("{}: {}".format(i, a_dictionary[i]))
