#!/usr/bin/python3

"""
Has the class User.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class User that inherits from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
