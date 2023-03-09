#!/usr/bin/python3
"""
main console of this
"""
import cmd
import models
from models.base_model import BaseModel
from shlex import split

class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = "(hbnb)"
    classes = ["BaseModel"]

    def do_quit(self, line):
        """
        quits
        :return: True
        """
        return True

    def do_EOF(self, line):
        """
        eof write in
        :return: True and prints an empty line
        """
        print()
        return True

    def emptyline(self):
        """
        :return: an empty line
        """

    def do_create(self, cls):
        """
        creates a new instance of BaseModel and then saves it to JSON
        Prints file Id too.
        """
        if not cls:
            return print("** class name missing **")
        if ' ' in cls:
            cls = cls.split(' ')[0]
        if cls not in HBNBCommand.classes:
            return print("** class doesn't exist **")
        else:
            new = eval(cls)()
            print(new.id)
            new.save()

    def do_show(self, args):
        """
        Prints the string representation of instance name + Id.
        """
        arguments = split(args)
        if len(arguments) == 0:
            return print("** class name missing **")
        if arguments[0] not in HBNBCommand.classes:
            return print("** class doesn't exist **")
        if len(arguments) == 1:
            print("** instance id missing **")
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
