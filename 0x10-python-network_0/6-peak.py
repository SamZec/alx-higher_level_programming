#!/usr/bin/python3
"""6-peak.py - a module containing thr funtion find_peak(list_of_integers)"""

def find_peak(list_of_integers):
    """
         a function that finds a peak in a list of unsorted integers.

         list_of_integers: integers to find peak from
    """
    if (list_of_integers is None or type(list_of_integers) is not list or
        len(list_of_integers) == 0):
            return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
            return max(list_of_integers)
    _len = len(list_of_integers)
    center = int(_len / 2)
    top = list_of_integers[center]
    if (top > list_of_integers[center - 1] and
            top > list_of_integers[center + 1]):
        return top
    if top <= list_of_integers[center - 1]:
        return find_peak(list_of_integers[:center])
    else:
        return find_peak(list_of_integers[center:])


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
