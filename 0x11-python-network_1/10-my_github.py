#!/usr/bin/python3
"""10-my_github.py - script for accessing github credentials"""

import requests
import sys


def github():
    """
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
    """
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    data = requests.get("https://api.github.com/user", auth=auth)
    print(data.json().get("id"))


if __name__ == '__main__':
    github()
