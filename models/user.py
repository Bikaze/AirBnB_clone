#!/usr/bin/python3
"""
This file contains one class i.e 'User'
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a User of this system

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
