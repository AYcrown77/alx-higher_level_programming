#!/usr/bin/python3
"""Module for appending string to a file"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
