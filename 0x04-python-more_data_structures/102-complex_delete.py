#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _keys = list(a_dictionary.keys())

    for _value in _keys:
        if value == a_dictionary.get(_value):
            del a_dictionary[_value]

    return (a_dictionary)
