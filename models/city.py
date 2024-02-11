#!/usr/bin/python3
"""
This file contains one class i.e 'City'
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class represents a City

    Attributes:
        name: string - empty string
        state_id: string - empty string: it will be the State.id
    """

    name = ""
    state_id = ""
