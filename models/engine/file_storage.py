#!/usr/bin/python3

""" File Storage Module """
import json

class FileStorage:
    """ FileStorage - serializes instances to a JSON file
        and deserializes JSON file to instances

    Args:

    """
    __file_path = "./file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        pass

    def all(self):
        """ Returns the dictionary __objects"""
        return __objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (dict): sets value for __object

        """
        self.__objects[obj.__class__.__name__ + '.' + str(obj)] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """

        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass

