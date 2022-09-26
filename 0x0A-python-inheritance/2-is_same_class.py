#!/usr/bin/python3
"""is_same_class module - no test cases needed"""


def is_same_class(obj, a_class):
    """check if object is exactly an instance of given class
    Args:
        obj: the object we're checking
        a_class: the class we are chevking for
    """
    return type(obj) == a_class
