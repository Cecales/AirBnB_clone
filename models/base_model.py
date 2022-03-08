#!/usr/bin/env python3
"""
Module for Base_Model class
This class will be used for the AirBnB clone console
"""

import models
from datetime import date, datetime
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
            for name, value in kwargs.items():
                if name != "__class__":
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
                    
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ instance
        """
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = self.created_at.isoformat(sep='T')
        new_dict["updated_at"] = self.updated_at.isoformat(sep='T')
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
