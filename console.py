#!/usr/bin/python3
import json
import models
from models.engine.file_storage import storage


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

    def do_create(self, arg):
        '''
            A function Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        '''
        if not arg:
            print("** class name is missing **")
            return

        try:
            class_name = arg.split[0]

            module = __import__('models.'+class_name, fromlist=[class_name])
            class_ = gettattr(module, class_name)

        except (ImportError, AttributeError):
            print("** class doesn't exist **")
            return

        instance = class_()
        f_name = "fiile.json"

        with open(f_name, 'a') as file:
            obj_dict = instance.to_dict()
            obj_dict["id"] = str(uuid.uuid4())
            json.dump(obj_dict["id"])

    def do_show(self, arg):
        '''
            A function that print the string representation of an instance
            Usage: show <class_name> <id>
        '''
        args = arg.splint()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
