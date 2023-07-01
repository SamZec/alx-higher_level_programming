#!/usr/bin/python3
"""5-hbtn_header.py - a module for making url requests"""

import requests
import sys


def request():
    """
    sends a request to the URL and displays the value of the variable
    'X-Request-Id' in the response header
    """
    data = requests.get(sys.argv[1])
    print(data.headers.get('X-Request-Id'))


if __name__ == '__main__':
    request()
