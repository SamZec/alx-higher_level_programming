#!/bin/bash
# script that takes in a URL and displays all HTTP methods allowed by server
curl -X OPTIONS -sI "$1" | grep 'allow:' | cut -c 8-
