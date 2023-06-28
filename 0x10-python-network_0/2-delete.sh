#!/bin/bash
# sends a DELETE request to a URL and displays the body of the response
curl -X DELETE -sL "$1"
