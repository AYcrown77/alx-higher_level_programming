#!/usr/bin/python3
"""module for base_geometry - no test cases needed"""


class BaseGeometry:
    """my BaseGeometry class"""
    def area(self):
        """method to calculate area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate a parameter as an integer

        Args:
            name (str): the name of the parameter.
            value (int): the parameter to validate.
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
