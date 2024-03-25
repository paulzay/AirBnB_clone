#!/usr/bin/python3

""" test class definition """
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        pass

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_instantiation(self):
        user_kwargs = {
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user_instance = User(**user_kwargs)
        self.assertEqual(user_instance.email, 'test@example.com')
        self.assertEqual(user_instance.password, 'password123')
        self.assertEqual(user_instance.first_name, 'John')
        self.assertEqual(user_instance.last_name, 'Doe')

    def test_methods(self):
        self.assertTrue(hasattr(self.user, 'save'))
        self.assertTrue(hasattr(self.user, 'to_dict'))
        self.assertTrue(hasattr(self.user, '__str__'))

if __name__ == '__main__':
    unittest.main()