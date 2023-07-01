#!/usr/bin/python3
"""2-post_email.py - a module for the function postEmail"""

import urllib.request
import urllib.parse
import sys


def postEmail():
    """
    sends a POST request to a URL with an email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    data = {'email': sys.argv[2]}
    data_parse = urllib.parse.urlencode(data)
    data_bytes = data_parse.encode('ascii')
    post = urllib.request.Request(sys.argv[1], data_bytes)
    with urllib.request.urlopen(post) as fs:
        print('Your email is: {}'.format(fs.read().decode('utf-8')))


if __name__ == '__main__':
    postEmail()
