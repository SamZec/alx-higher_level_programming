#!/bin/bash
# displays content size of a response body from a url
curl -s "$1" | wc -c
