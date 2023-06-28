#!/bin/bash
# sends a request to 0.0.0.0:5000/catch_me and get "You got me!" as a response.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
