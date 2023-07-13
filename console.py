#!/usr/bin/python3
'''Module of AirBNB console'''
import cmd
from shlex import split
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage as storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    valid_models = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                    "Review"]
    valid_cmds = ["all", "count", "show", "destroy", "update"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Ensures that previous command is not run twice"""

    def do_create(self, cls):
        """Creates a new instance, saves it, and prints id"""
        if not cls:
            return(print("** class name missing **"))
        if ' ' in cls:
            cls = cls.split(' ')[0]
        if cls not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
        else:
            new_class = eval(cls)()
            print(new_class.id)
            new_class.save()

    def do_show(self, args):
        """Prints the str repr of an instance with class name and id"""
        params = sp(args)
        if len(params) == 0:
            return(print("** class name missing **"))
        if params[0] not in HBNBCommand.valid_models:
            return(print("** class doesn't exist **"))
        if len(params) == 1:
            print("** instance id missing **")
        else:
            try:
                k = params[0] + '.' + params[1]
                if k in models.storage.all():
                    print(models.storage.all()[k])
                else:
                    print("** no instance found **")
            except Exception as e:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        params = sp(args)
        if len(params) == 0:
            return(print("** class name missing **"))
        if params[0] not in HBNBCommand.valid_models:
            return(print("** class doesn't exist **"))
        if len(params) == 1:
            print("** instance id missing **")
        else:
            try:
                k = params[0] + '.' + params[1]
                if k in models.storage.all():
                    del models.storage.all()[k]
                    models.storage.save()
                else:
                    print("** no instance found **")
            except Exception as e:
                print("** class doesn't exist **")

    def do_all(self, cls_name):
        """Prints all str repr of all instances of class name"""
        str_list = []
        if not cls_name:
            for v in models.storage.all().values():
                str_list.append(str(v))
        else:
            if cls_name not in HBNBCommand.valid_models:
                print("** class doesn't exist **")
                return
            for k, v in models.storage.all().items():
                left = k.split('.')[0]
                if left == cls_name:
                    str_list.append(str(v))
        print(str_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        params = sp(args)
        if len(params) == 0:
            return(print("** class name missing **"))
        if params[0] not in HBNBCommand.valid_models:
            return(print("** class doesn't exist **"))
        if len(params) == 1:
            return(print("** instance id missing **"))
        k = params[0] + "." + params[1]
        if k not in models.storage.all().keys():
            return(print("** no instance found **"))
        if len(params) == 2:
            print("** attribute name missing **")
        elif len(params) == 3:
            print("** value missing **")
        else:
            k = params[0] + '.' + params[1]
            val = params[3]
            try:
                if val.isdigit():
                    val = int(val)
                elif float(val):
                    val = float(val)
            except ValueError:
                pass
            if k in models.storage.all():
                setattr(models.storage.all()[k], params[2], params[3])
                models.storage.save()


if __name__ == '__main__':
    ls = ['BaseModel', 'User', 'City', 'State', 'Review', 'Amenity', 'Place']
    HBNBCommand().cmdloop()
