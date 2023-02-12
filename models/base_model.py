#!/usr/bin/python3
"""BaseModel -  defines all common attributes/methods for other classes"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """ BaseModel -  defines all common attributes/methods for other classes

        Args:
            args (list): a dynamic list of arguments
            kwargs (dict): dictionary of keyword arguments
    """

    def __init__(self, *args, **kwargs):
        """ BaseModel """
        if not kwargs:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

            storage.new(self)

        else:
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")


    def __str__(self):
        """ String representation of base object"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Save - updates the public instance
            attribute updated_at with the current datetime"""
        update_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all
            keys/values of __dict__ of the instance"""

        newDict = {"__class__": self.__class__.__name__}
        newDict.update(self.__dict__)

        return newDict

