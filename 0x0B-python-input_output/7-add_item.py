#!/usr/bin/python3
# 7-add_item.py
"""A script that adds arguments to python list"""

from sys import argv


save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

_len = len(argv)
filename = 'add_item.json'
obj = []

try:
    obj = load_from(filename)
except Exception:
    obj = []

for i in range(1, _len):
    obj.append(argv[i])
save_to(obj, filename)
