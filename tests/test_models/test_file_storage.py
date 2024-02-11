#!/usr/bin/python3

import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def test_allmethod(self):
        # Test the All method of FileStorage method

        # Creating an instance
        file_storage_instance = FileStorage()

        # Checking the value of the dictionary of created file
        self.assertIsInstance(file_storage_instance.all(), dict)
        self.assertNotEqual(len(file_storage_instance.all()), 0)

    def test_new(self):
        # A function to test out the new method inside FileStorage

        # An instance of the base class
        file_storage_instance = FileStorage()

        # An instance of the file storage 
        base_model_instance = BaseModel()

        # Calling new method with base class model
        file_storage_instance.new(base_model_instance)

        # Checking if the object added to __objects with the correct key
        expected_key = "{}.{}".format(base_model_instance.__class__.__name__, base_model_instance.id)
        self.assertIn(expected_key, file_storage_instance.all())

if __name__ == '__main__':
    unittest.main()
