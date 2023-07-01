#!/usr/bin/python3
"""8-json_api.py - a module for sending url requests"""

import requests
import sys


def request():
    """
     sends a POST request to http://0.0.0.0:5000/search_user
     with the letter as a parameter.

     The letter must be sent in the variable q
     If no argument is given, set q=""
     If the response body is properly JSON formatted and not empty, display
     the id and name like this: '[<id>] <name>'
     Otherwise:
        Display 'Not a valid JSON' if the JSON is invalid
        Display 'No result' if the JSON is empty
    """
    payload = {'q': ""}
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        payload = {'q': sys.argv[1]}
    data = requests.post(url, payload)
    try:
        data_json = data.json()
        if data_json:
            print("[{}] {}".format(data_json['id'], data_json['name']))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")


if __name__ == '__main__':
    request()
