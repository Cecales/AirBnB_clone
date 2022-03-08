#!/usr/bin/python3
"""Model write class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel
    Attributes:
        email (str): Public class attribute for User's email
        password (str): Public class attribute for User's password
        first_name (str): Public class attribute for User's first name
        last_name (str): Public class attribute for User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init method for User class"""
        super().__init__(*args, **kwargs)
