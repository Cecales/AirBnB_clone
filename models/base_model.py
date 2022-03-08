#!/usr/bin/env python3
"""
Module for Base_Model class
This class will be used for the AirBnB clone console
"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Class for base model"""

    def __init__(self, *args, **kwargs):
        """
        Instance of a Base instance
        Args:
        *args: variables length argument list not used
        **kwargs: (key - value) pair of atrributtes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        date = '%Y-%m-%dT%H:%M:%S.%f'
                        value = datetime.strptime(value, date)
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the object"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        
        return new_dict
