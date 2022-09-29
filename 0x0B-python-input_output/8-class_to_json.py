#!/usr/bin/python3
"""My class_to_json module"""
import json


def class_to_json(obj):
    """function that returns the dictionary description/
       with simple data structure
    """
    return obj.__dict__

