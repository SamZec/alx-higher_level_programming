#!/usr/bin/python3
"""0-hbtn_status.py - a module for fetchURL function"""

import urllib.request


def fetchURL():
    """
    a function that fetch https://alx-intranet.hbtn.io/status with urllib
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as fs:
        f = fs.read()
        print("Body response:")
        print("\t- type: {}".format(type(f)))
        print("\t- content: {}".format(f))
        print("\t- utf8 content: {}".format(f.decode()))


if __name__ == '__main__':
    fetchURL()
