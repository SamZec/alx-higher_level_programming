#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        pass
    _mystring = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ''
            _mystring += i
        _mystring += i
    return _mystring
