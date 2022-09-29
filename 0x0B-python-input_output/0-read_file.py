#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="UTF8") as f:
        read_data = f.read()
        print(read_data, end="")
