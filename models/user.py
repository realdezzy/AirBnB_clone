#!/usr/bin/python3

""" User submodule """
from models.base_model import BaseModel


class User(BaseModel):
    """ User - Holds data for a specific user
        Attributes:
            email (str): Class attribute for User email
            password (str): Class attribute for User password
            first_name (str): Class attribute for User first name
            last_name (str): Class attribute for User last name

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""


    def __init__(self, *args, **kwargs):
        """
        init method for User class
        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
