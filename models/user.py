#!/usr/bin/python3
"""
This file contains one class i.e 'User'
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a User of this system"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
