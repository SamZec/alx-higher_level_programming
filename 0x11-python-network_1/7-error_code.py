#!/usr/bin/python3
"""7-error_code.py - a module for making url requests"""

import requests
import sys


def request():
    """
    sends a request to a URL and displays the body of the response.

    If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
    """
    data = requests.get(sys.argv[1])
    if data.status_code >= 400:
        print("Error code: {}".format(data.status_code))
    else:
        print(data.text)


if __name__ == '__main__':
    request()
