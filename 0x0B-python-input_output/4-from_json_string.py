#!/usr/bin/python3
"""My 4-from_json_string module"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
