#!/usr/bin/python3
"""6-post_email.py - a module for making url requests"""

import requests
import sys


def request():
    """
    sends a POST request to a URL with an email as a parameter,
    and finally displays the body of the response.
    """
    data = {'email': sys.argv[2]}
    _post = requests.post(sys.argv[1], data)
    print(_post.text)


if __name__ == '__main__':
    request()
