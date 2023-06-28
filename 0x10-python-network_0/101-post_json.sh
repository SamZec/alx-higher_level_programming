#!/bin/bash
# script that sends a JSON POST request to a URL and displays the body of the response.
curl -s -X POST -H "Content-Type: Application/json" -d @"$2" "$1"
