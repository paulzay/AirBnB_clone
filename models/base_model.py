#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
    	if not kwargs:
    		self.id = str(uuid.uuid4())
    		self.created_at = datetime.now()
    		self.updated_at = datetime.now()
    	else:
            for i in kwargs:
            	if i == "id":
            		self.id = kwargs[i]
            	elif i == "created_at":
            		self.created_at = kwargs[i]
            	elif i == "updated_at":
            		self.updated_at = kwargs[i]


    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
