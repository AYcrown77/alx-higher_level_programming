#!/usr/bin/python3

"""My Square module"""


class Square:
    """define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a square

        Args:
            size: length of a side of square

        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"
        The properties of size as the len of a side of square

        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        """property of the coordinate of this square

        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this square

        Args: value as a tuple of 2 positive integers

        Raises:
            TypeError: if value is not a tuple or is < 0
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for x in range(self.position[0]):
                pos += " "
            for x in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):

        """print the square in position"""
        print(self.pos_print(), end='')
