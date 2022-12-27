#!/bin/bash
# send a POST request to the passed URL using curl, and display the body of the response
curl -s -X POST -d "email=test@gmail.con&subject=I will always be here foe PLD" "$1"
