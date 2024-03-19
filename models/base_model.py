#!/usr/bin/python3

import uuid
import datetime

class BaseModel:

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        print("[<class name>] (<self.id>) <self.__dict__>")
    
    def save(self):
        pass

    def to_dict(self):
        pass
