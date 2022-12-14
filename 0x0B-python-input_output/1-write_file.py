#!/usr/bin/python3
"""my write_file module"""


def write_file(filename="", text=""):
    """writes a string to a text file\
       and returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
