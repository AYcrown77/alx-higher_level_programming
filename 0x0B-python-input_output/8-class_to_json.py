#!/usr/bin/python3
"""My class_to_json module"""


def class_to_json(obj):
    """function that returns the dictionary description
    """
    return obj.__dict__
