#!/usr/bin/python3
"""3-error_code.py - a module for sending HTTP request"""

import urllib.request
import sys


def errorCode():
    """
    sends a request to a, manage urllib.error.HTTPError exceptions
    and print: Error code: followed by the HTTP status code
    """
    try:
        with urllib.request.urlopen(sys.argv[1]) as fs:
            f = fs.read()
            print(f.decode())
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    errorCode()
