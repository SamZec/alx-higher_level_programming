#!/usr/bin/python3
"""4-hbtn_status.py - a module for making url requests"""

import requests


def request():
    """
    fetches https://alx-intranet.hbtn.io/status
    """
    data = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(data.text)))
    print('\t- content: {}'.format(data.text))


if __name__ == '__main__':
    request()
