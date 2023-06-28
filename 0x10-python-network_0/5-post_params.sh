#!/bin/bash
# sends a POST request a URL, and displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
