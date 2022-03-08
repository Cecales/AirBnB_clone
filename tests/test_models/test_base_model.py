#!/usr/bin/python3
"""Test BaseModel class"""
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_base(unittest.TestCase):
    """
    class testing BaseModel class' methods
    """
    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.instance = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Final step"""
        del cls.instance

    def test_pep8_conformance(self):
        """Test that base_model.py file conform to PEP8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.checkfiles(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc(self):
        """Test documentation BaseModel"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_base_atrr(self):
        """Test BaseModel attributes"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertEqual(len(base.id), 36)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_save(self):
        """Test save method"""
        past_update = self.instance.updated_at
        self.instance.save()
        self.assertIsNot(self.instance.created_at, self.instance.updated_at)
        self.assertIsNot(past_update, self.instance.updated_at)

    def test_to_dict_method(self):
        """BaseModel to_dict method creates accurate dictionary"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], base.id)
        self.assertEqual(base_dict['__class__'], type(base).__name__)
        self.assertEqual(base_dict['created_at'], base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
