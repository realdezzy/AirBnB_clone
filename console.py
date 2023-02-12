#!/usr/bin/python3
""" Command interpreter program"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ Entry point for the command interpreter """

    prompt = '(hnbn) '
#intro = "Simple command processor example."
    doc_header = "Documented commands (type help <topic>)"
    ruler = "="

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self, line):
        """Quit console """
        return True
    def help_quit(self):
        """ How to quit interpreter """
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
