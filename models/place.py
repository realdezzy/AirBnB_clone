#!/usr/bin/python3

""" Place submodule """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place - Holds data for a specific place

        Attributes:
            city_id (str): The City id.
            user_id (str): The User id.
            name (str): The name of the place.
            description (str): The description of the place.
            number_rooms (int): The number of rooms of the place.
            number_bathrooms (int): The number of bathrooms of the place.
            max_guest (int): The maximum number of guests of the place.
            price_by_night (int): The price by night of the place
            latitude (float): The latitude of the place.
            longitude (float): The longitude of the place.
            amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
