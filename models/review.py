#!/usr/bin/python3
"""
This file contains one class i.e 'Review'
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class represents a Review

    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
