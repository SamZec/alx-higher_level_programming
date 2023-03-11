#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    _len = len(my_list) - 1
    while _len >= 1:
        _len1 = 0
        while _len1 < _len:
            if my_list[_len1] < my_list[_len1 + 1]:
                temp = my_list[_len1]
                my_list[_len1] = my_list[_len1 + 1]
                my_list[_len1 + 1] = temp
            _len1 += 1
        _len -= 1
    for i in my_list:
        print("{:d}".format(i))
