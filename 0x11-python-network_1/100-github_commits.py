#!/usr/bin/python3
"""100-github_commits.py - script for accessing github commits"""

import requests
import sys


def github():
    """
    prints last ten commits from a github repository passed as arguments

    args:
            1st: repository name
            2nd: owner name
    """
    url = "https://api.github.com/repos/{}/{}/commits".format(
                sys.argv[2], sys.argv[1])
    data = requests.get(url)
    data_list = data.json()
    try:
        for i in range(10):
            data_dict = dict(data_list[i])
            _id = data_dict.get('sha')
            name = data_dict.get('commit').get('author').get('name')
            print("{}: {}".format(_id, name))
    except Exception as e:
        pass


if __name__ == '__main__':
    github()
