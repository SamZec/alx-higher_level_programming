#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    _dicts = sorted(a_dictionary.items(), key=lambda x: x[1])
    _dict = dict(_dicts)
    return list(_dict)[-1]
