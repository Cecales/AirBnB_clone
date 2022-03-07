#!/usr/bin/python3
"""
Module to write class state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel
    Attribute:
        name (str): Public class attribute for State's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method for State class
        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
