#!/usr/bin/python3
"""My load_from_json_file module"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""
    with open(filename, 'r') as new:
        return json.load(new)
