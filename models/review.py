#!/usr/bin/python3

"""
Has the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class Review that inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
