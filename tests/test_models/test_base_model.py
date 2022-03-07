#!/usr/bin/python3
"""Test Basemodel class"""
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel

class test_base(unittest.TestCase):
    """
    class testing BaseModel class' methods
    """
    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.instance = BaseModel()

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
    
if __name__ == '__main__':
    unittest.main()
