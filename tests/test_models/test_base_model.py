import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        expected_str = f"[BaseModel] \
                ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    @patch('models.base_model.datetime')
    def test_save(self, mock_datetime):
        mock_datetime.now.return_value = \
                datetime(2023, 5, 16, 14, 27, 12, 456789)
        self.base_model.save()
        self.assertEqual(self.base_model.updated_at,
                         mock_datetime.now.return_value)

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        self.assertEqual(base_model_dict['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'],
                         self.base_model.updated_at.isoformat())

    def test_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': '2023-05-16T14:27:12.456789',
            'updated_at': '2023-05-16T14:27:12.456789'
        }
        base_model_kwargs = BaseModel(**kwargs)
        self.assertEqual(base_model_kwargs.id, 'test_id')
        self.assertEqual(base_model_kwargs.created_at,
                         datetime(2023, 5, 16, 14, 27, 12, 456789))
        self.assertEqual(base_model_kwargs.updated_at,
                         datetime(2023, 5, 16, 14, 27, 12, 456789))


if __name__ == '__main__':
    unittest.main()
