#!/usr/bin/python3
"""my save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as new:
        return json.dump(my_obj, new)
