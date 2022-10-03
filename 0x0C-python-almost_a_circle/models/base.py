#!/usr/bin/python3
"""Module for base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of instance attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), 'w', encoding='utf-8')\
                as content:
            content.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """retrieve __dict__ from json"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """loads an instance"""
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """retrieve string from file"""
        from os import path
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            list_dicts = cls.from_json_string(f.read())
            return [cls.create(**arg) for arg in list_dicts]
