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

    def test_save(self):
        # Creating instances of the BaseModel class
    
        first_model = BaseModel()
        second_model = BaseModel()

        # Adding instances to the __objects
        FileStorage._FileStorage__objects["BaseModel.{}".format(first_model.id)] = first_model
        FileStorage._FileStorage__objects["BaseModel.{}".format(second_model.id)] = second_model

        # Calling save method
        FileStorage.save(FileStorage)

        # Read the contents of the file
        with open(FileStorage._FileStorage__file_path, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)

        # Verify the contents
        expected_data = {
            "BaseModel.{}".format(first_model.id): first_model.to_dict(),
            "BaseModel.{}".format(second_model.id): second_model.to_dict()
        }

        self.assertEqual(saved_data, expected_data)


if __name__ == '__main__':
    unittest.main()
