#!/usr/bin/python3

"""
This program contains the entry point of the command interpreter
"""
import cmd
import json
import uuid
from models.base_model import BaseModel

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

        try:
            class_name = arg.split()[0]
            module = __import__('models.' + class_name, fromlist=[class_name])
            class_ = getattr(module, class_name)

        except (ImportError, AttributeError):
            print("** class doesn't exist **")
            return

        instance = class_()
        instance.save()
        print(instance.id)

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

        class_name, obj_id = args[0], args[1]

        try:
            module = __import__('models.' + class_name, fromlist=[class_name])
            class_ = getattr(module, class_name)
        except (ImportError, AttributeError):
            print("** class doesn't exist **")
            return

        filename = "file.json"
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("** no instance found **")
            return

        instance_key = "{}.{}".format(class_name, obj_id)
        if instance_key in data:
            # Create an instance and print its string representation
            instance = class_(**data[instance_key])
            print(instance)
        else:
            print("** no instance found **")

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

        class_name, obj_id = args[0], args[1]

        try:
            module = __import__('models.' + class_name, fromlist=[class_name])
            class_ = getattr(module, class_name)
        except (ImportError, AttributeError):
            print("** class doesn't exist **")
            return

        filename = "file.json"
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("** no instance found **")
            return

        instance_key = "{}.{}".format(class_name, obj_id)
        if instance_key in data:
            del data[instance_key]
            with open(filename, 'w') as file:
                json.dump(data, file)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        '''
        A function that prints all string representation of all instances
        based or not on the class name.
        Usage: $ all <Class name> or $ all
        '''
        filename = "file.json"

        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        if not arg:
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                module = __import__('models.' + class_name, fromlist=[class_name])
                class_ = getattr(module, class_name)
                instance = class_(**value)
                print(instance)
        else:
            try:
                class_name = arg.split()[0]
                module = __import__('models.' + class_name, fromlist=[class_name])
                class_ = getattr(module, class_name)
            except (ImportError, AttributeError):
                print("** class doesn't exist **")
                return

            for key, value in data.items():
                if key.startswith(class_name):
                    instance = class_(**value)
                    print(instance)

    def do_update(self, arg):
        '''
        A function that updates an instance based on the class name and id
        by adding or updating an attribute (save the change into the JSON file).
        Usage: $ update <Class name> <id> <attribute name> "<attribute value>"
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
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        class_name, obj_id, attr_name, attr_value = args[0], args[1], args[2], args[3]

        try:
            module = __import__('models.' + class_name, fromlist=[class_name])
            class_ = getattr(module, class_name)
        except (ImportError, AttributeError):
            print("** class doesn't exist **")
            return

        filename = "file.json"
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("** no instance found **")
            return

        instance_key = "{}.{}".format(class_name, obj_id)
        if instance_key in data:
            instance = class_(**data[instance_key])
            setattr(instance, attr_name, attr_value.strip('"'))
            instance.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()