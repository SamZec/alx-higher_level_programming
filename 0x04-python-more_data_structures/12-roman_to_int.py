#!/usr/bin/python3
def roman_to_int(roman_string):
    _dict = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "CM": 900,
        "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400
    }
    if not isinstance(roman_string, str):
        return 0
    _int = 0
    upd = 0
    _len = len(roman_string)
    while upd < _len:
        if upd + 1 < _len and roman_string[upd:upd + 2] in _dict:
            _int += _dict[roman_string[upd:upd + 2]]
            upd += 2
        else:
            _int += _dict[roman_string[upd]]
            upd += 1
    return _int
