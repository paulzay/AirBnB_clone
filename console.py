#!/usr/bin/python3

""" class definition """
import json
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
import models


class HBNBCommand(cmd.Cmd):
    """ cmd class """
    prompt = '(hbnb) '
    file = None

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "State": State,
        "Review": Review,
        "Place": Place
    }

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ END OF FILE """
        return True

    def emptyline(self):
        """ Dont execute anything """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            try:
                new_model = self.classes[args[0]]()
                new_model.save()
                print(new_model.id)
            except Exception as e:
                print("** Error creating instance **")
                print(e)

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        args = args.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
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
        elif args[0] not in self.classes:
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
        data_list = []
        if not args:
            for item in models.storage.all().values():
                data_list.append(item.__str__())
                print(data_list)
        else:
            args = args.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for item in models.storage.all().values():
                    if args[0] == item.__class__.__name__:
                        data_list.append(item.__str__())
                print(data_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        args = args.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing ** ")
        elif len(args) < 4:
            print("** value missing **")
        elif len(args) > 5:
            return
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            instance = models.storage.all().get(key)

            if not instance:
                print("** no instance found **")
            else:
                pass
                data = models.storage.all()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
