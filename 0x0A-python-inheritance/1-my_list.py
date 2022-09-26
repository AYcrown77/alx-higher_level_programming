#!/usr/bin/python3

"""A module to print a list in ascending order"""


class MyList(list):
    """A class to customize the list class"""
    def print_sorted(self):
        """prints sorted list method"""
        print(sorted(self))
