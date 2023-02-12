#!/usr/bin/python3

""" User submodule """
from models.base_model import BaseModel


class User(BaseModel):
    """ User - Holds data for a specific user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
