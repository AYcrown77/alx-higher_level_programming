#!/usr/bin/python3
"""Write a pythgon script that takes in a  letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=data)
    try:
        right = response.json()
        if not right:
            print("No result")
        else:
            print("[{}] {}".format(right.get("id"), right.get("name")))
    except ValueError:
        print("Not a valid JSON")
