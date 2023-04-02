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
        quits the console
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

    def do_destroy(self, args):
        """
        Deletes an instance based on class name and id
        :param args: the given paramatres
        """
        params = split(args)
        if len(params) == 0:
            return print("** class name missing **")
        if params[0] not in HBNBCommand.classes:
            return print("** class doesn't exist **")
        if len(params) < 2:
            return print("** instance id missing **")
        else:
            try:
                instance = params[0] + '.' + params[1]
                if instance in models.storage.all():
                    del models.storage.all()[instance]
                    models.storage.save()
                else:
                    print("** no instance found **")
            except Exception as e:
                print("** class doesn't exist **")

    def do_all(self, cls_name):
        """
        prints the string representation
        :param cls_name: of instances based on classes
        """
        str_list = []
        if not cls_name:
            for v in models.storage.all().values():
                str_list.append(str(v))
        else:
            if cls_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
            for i, j in models.storage.all().items():
                find = i.split(".")[0]
                if i == cls_name:
                    str_list.append(str(j))
        print(str_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        """
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
    HBNBCommand().cmdloop()
