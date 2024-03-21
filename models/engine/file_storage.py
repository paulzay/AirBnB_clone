#!/usr/bin/env python3

"""class definition"""
import json
from models.base_model import BaseModel


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
                self.__objects = {
                    key: BaseModel(**value) for key, value in obj_dict.items()
                }
        except FileNotFoundError:
            pass
