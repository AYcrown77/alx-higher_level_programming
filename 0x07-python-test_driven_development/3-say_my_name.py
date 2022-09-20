#!/usr/bin/python3
"""say my name module"""


def say_my_name(first_name, last_name=""):
    """prints your name, first and last. Last not compulsory

    Args:
        first_name: a string
        last_name: another string
    Raises:
        TypeError: if either name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

