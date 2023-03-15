#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        pass

    _mylist = []
    for i in my_list:
        if i == search:
            _mylist.append(replace)
        else:
            _mylist.append(i)
    return _mylist
