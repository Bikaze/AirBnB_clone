#!/usr/bin/python3

"""
This program contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage

class HBNBCommand(cmd.Cmd):
    """This is a Cmd subclass representing our command interpreter"""
    prompt = "(hbnb) "

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
            print("** class name missing **")
            return

        args = arg.split()
        class_repr = globals().get(args[0]) 
        if len(args) != 1 or class_repr is None:
            print("** class doesn't exist **")
        else:
            class_obj = class_repr()
            print(class_obj.id)

    def do_show(self, arg):
        '''
        A function that shows the string representation of a class name
        and the id given
        Usage: $ show <Class name> <id>
        '''
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        objects = storage.all()
        obj = objects.get(key)
        
        if not obj:
            print("** no instance found **")
            return
        else:
            print(obj)

    def do_destroy(self, arg):
        '''
        A function that deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage: $ destroy <Class name> <id>
        '''
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        objects = storage.all()
        obj = objects.get(key)

        if not obj:
            print("** no instance found **")
            return
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        '''
        A function that prints all string representation of all instances
        based or not on the class name.
        Usage: $ all <Class name> or $ all
        '''
        
        args = arg.split()
        objects = storage.all()
        if len(args) > 1 or (len(args) == 1 and globals().get(args[0]) is None):
            print("** class doesn't exist **")
            return
        else:
            all_objects = []
            for key, value in objects.items():
                if len(args) == 1 and key.split('.')[0] != args[0]:
                    pass
                else:
                    all_objects.append(value.__str__())
            print(all_objects)

    def do_update(self, arg):
        '''
        A function that updates an instance based on the class name and id
        by adding or updating an attribute (save the change into the JSON file).
        Usage: $ update <Class name> <id> <attribute name> "<attribute value>"
        '''
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if not globals().get(args[0]):
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        objects = storage.all()
        obj = objects.get(key)

        if not obj:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        value = args[3]
        if value.replace('.', '', 1).isnumeric():
            if value.replace('.', '', 1) == value:
                value = int(value)
            else:
                value = float(value)
        else:
            if value[0] == '"' and value[-1] == '"':
                value = value.strip('"')
            if value[0] == "'" and value[-1] == "'":
                value = value.strip("'")
            setattr(objects[key], args[2], value)
            objects[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
