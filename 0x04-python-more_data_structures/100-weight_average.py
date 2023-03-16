#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    _sum = div = 0
    _list = list(map(lambda x: x[0] * x[1], my_list))
    _list1 = list(map(lambda x: x[1], my_list))
    for i in range(len(_list)):
        _sum += _list[i]
        div += _list1[i]
    return _sum / div
