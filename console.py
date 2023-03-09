#!/usr/bin/python3
"""
main console of this
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = "(hbnb)"

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
