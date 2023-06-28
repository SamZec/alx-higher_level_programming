#!/bin/bash
# script that takes in a URL and displays all HTTP methods allowed by server
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-
