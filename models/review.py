#!/usr/bin/python3

""" class definition """
from models.base_model import BaseModel


class Review(BaseModel):
    """docstring for Review"""
    place_id = ''
    user_id = ''
    text = ''
