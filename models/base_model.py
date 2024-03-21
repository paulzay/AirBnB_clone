#!/usr/bin/python3

""" class definition """
import uuid
from datetime import datetime
import models


class BaseModel:
    """base model class"""
    def __init__(self, *args, **kwargs):
        """
        Initialize
        Args:
            *args: Unused positional arguments.
            **kwargs: Key-value pairs of attributes.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)

    def __str__(self):
        """ string representation of class"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """function to save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """function to return dict"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
