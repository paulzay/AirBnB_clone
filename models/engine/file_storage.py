#!/usr/bin/env python3

"""class definition"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {
            key: value.to_dict() for key, value in self.__objects.items()
        }
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                classes = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "Amenity": Amenity,
                    "State": State,
                    "Review": Review,
                    "City": City,
                    "Place": Place
                    }

                for key, obj_dict in obj_dict.items():
                    class_name = obj_dict["__class__"]
                    self.__objects[key] = classes[class_name](**obj_dict)
        except FileNotFoundError:
            return
