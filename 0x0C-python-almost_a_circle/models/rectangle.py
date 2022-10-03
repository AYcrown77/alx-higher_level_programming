#!/usr/bin/python3
"""Rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """my Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init magic"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of a rectangle"""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """get height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of a rectangle"""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """get x of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x of a rectangle"""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """get y of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y of a rectangle"""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name,  value, eq=True):
        """check the value as int and >= 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """find area of a rectangle"""
        return self.width * self.height

    def display(self):
        """dispay the rectangle using #"""
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """str info about a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}
