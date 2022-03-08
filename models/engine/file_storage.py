#!/usr/bin/env python3
"""Class FileStorage that serializes instances to a JSON file"""

import json
import os.path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """Class Filestorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj .id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the json file path"""
        new_dict = {}
        for key, value in self.__objects.itmes():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w',) as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the json file to __objects"""
        new_classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'Amenity': Amenity,
            'Place': Place,
            'City': City,
            'Review': Review
        }
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                new_dict = json.load(file)
            for key, value in new_dict.items():
                object = value['__class__']
                objects = object + '(**value)'
                self.__objects[key] = eval(objects)
