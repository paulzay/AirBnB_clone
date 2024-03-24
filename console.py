#!/usr/bin/python3

""" class definition """
import json
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """ cmd class"""
    intro = 'Welcome to my shell! Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """ Quit command to exit the program """
        print('exiting')
        return True

    def do_EOF(self, arg):
        """ END OF FILE """
        return True

    def do_emptyline(self):
        """ Dont execute anything """
        return ""

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        args = args.split()

        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            instance = models.storage.all().get(key)

            if not instance:
                print("** no instance found **")
            else:
                print(str(instance))

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        args = args.split()

        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            instance = models.storage.all().get(key)

            if not instance:
                print("** no instance found **")
            else:
                data = models.storage.all()
                del data["{}.{}".format(args[0], args[1])]
                models.storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        if not args:
            print('allat')
        else:
            args = args.split()
            if args[0] != 'BaseModel':
                print("** class doesn't exist **")
            else:
                pass

    def do_update(self, args):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
