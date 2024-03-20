#!/usr/bin/python3

import uuid
from datetime import datetime
""" class definition"""


class BaseModel:
	"""base model class"""
	def __init__(self, *args, **kwargs):
		""" Initialize """
		if not kwargs:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
		else:
			for key, value in kwargs.items():
				if key == "id":
					self.id = value
				elif key == "created_at":
					self.created_at = datetime.fromisoformat(value)
				elif key == "updated_at":
					self.updated_at = datetime.fromisoformat(value)

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
