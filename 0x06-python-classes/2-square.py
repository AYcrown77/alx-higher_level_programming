#!/usr/bin/python3

"""My Square module"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """Create a square

        Args:
            size: length of size

        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
