#!/usr/bin/python3

""" City submodule """
from models.base_model import BaseModel


class City(BaseModel):
    """ City - Holds data for a specific city"""

    state_id = ""
    name = ""
