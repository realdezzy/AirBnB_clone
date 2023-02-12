#!/usr/bin/python3

""" Review submodule """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review - Holds data for a specific review"""

    place_id = ""
    user_id = ""
    text = ""
