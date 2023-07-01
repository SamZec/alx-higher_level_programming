#!/usr/bin/python3
"""1-hbtn_header.py - a module for getId function"""

import urllib.request
import sys


def getId():
    """
    sends a request to the URL and displays the value of the X-Request-Id
    variable found in the header of the response.
    """
    with urllib.request.urlopen(sys.argv[1]) as fs:
        f = fs.headers.get('X-Request-Id')
        print(f)


if __name__ == "__main__":
    getId()
