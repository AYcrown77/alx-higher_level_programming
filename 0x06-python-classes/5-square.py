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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Retrns the current square area"""

        return self.__size ** 2

    def my_print(self):
        """print the square in #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
