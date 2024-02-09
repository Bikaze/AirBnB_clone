#!/usr/bin/python3

"""
This program contains the entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """This is a Cmd subclass representing our command interpreter"""
    prompt="(hbnb) "

    def do_EOF(self, line):
        """Exit the interpreter"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Should do nothing when Enter key is pressed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
