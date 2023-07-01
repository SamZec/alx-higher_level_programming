#!/usr/bin/python3
"""10-my_github.py - script for accessing github credentials"""

import requests
import sys


def github():
    """
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
    """
    header = {
                "Accept": "application/vnd.github+json",
                "Authorization": "Bearer {}".format(sys.argv[2]),
                "X-GitHub-Api-Version": "2022-11-28"
            }
    url = 'https://api.github.com/{}'.format(sys.argv[1])
    data = requests.get(url, headers=header)
    try:
        data = requests.get(url, headers=header)
        data_dict = data.text
        print(data_dict.get('id'))
    except Exception as e:
        print("None")


if __name__ == '__main__':
    github()
