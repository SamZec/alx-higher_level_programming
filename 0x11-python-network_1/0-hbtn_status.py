#!/usr/bin/python3
"""0-hbtn_status.py - a module for fetchURL function"""

import urllib.request


def fetchURL():
    """
    a function that fetch https://alx-intranet.hbtn.io/status with urllib
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as fs:
        f = fs.read()
        body = "Body response:\n"
        _type = "    - type: {}\n".format(type(f))
        content = "    - content: {}\n".format(f)
        _utf8 = "    - utf8 content: {}".format(f.decode())
        print(body + _type + content + _utf8)


if __name__ == '__main__':
    fetchURL()
