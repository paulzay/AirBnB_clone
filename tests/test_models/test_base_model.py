#!/usr/bin/python3

""" test class definition """
import unittest
from models.base_model import BaseModel
import models


class BaseModelTest(unittest.TestCase):
    """docstring for class"""
    def test_save(self):
        old_len = len(models.storage.all())
        mid_len = len(models.storage.all())
        new_model = BaseModel()
        new_model.name = "Root User"
        new_model.my_num = 12
        new_model.save()
        self.assertEqual(old_len, mid_len)

    def test_to_dict(self):
        """ test to_dict """
        pass

    def test__str__(self):
        """ test __str__ """
        pass


if __name__ == '__main__':
    unittest.main()
