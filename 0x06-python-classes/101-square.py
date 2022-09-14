#!/usr/bin/python3
"""my square module"""


class Square:
    """define a Square"""

    def __str__(self):
        """teach python to print the square my way"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """initialize the square with this
        Args:
            size: a side of square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """property of the length of a side of square

        Raises:
                TypeError: if size is not an int
                ValueError: if size is < 0
        """

        return self.__size
