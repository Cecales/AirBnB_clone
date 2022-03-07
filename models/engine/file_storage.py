#!/usr/bin/env python3
"""Class FileStorage that serializes instances to a JSON file"""

import json
import os.path
from os import read
from models.base_model import BaseModel


class FileStorage:
    """Class Filestorage"""
    def __init__(self):
        """Innitializaes FilesStorage"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the json file path"""
        dictionary = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                dictionary[key] = obj.to_dict()
            json.dump(dictionary, f)

    def reload(self):
        """Deserialize the json file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                new_object = key.split('.')
                class_name = new_object[0]
                self.new(eval("{}".format(class_name))(**value))
        except FileNotFoundError:
            pass
