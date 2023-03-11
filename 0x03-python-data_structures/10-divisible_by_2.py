#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        pass
    _mylist = []
    for i in my_list:
        if i % 2 == 0:
            _mylist.append(True)
        else:
            _mylist.append(False)
    return _mylist
