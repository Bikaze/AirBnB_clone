#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        # Test the initialisation of BaseModel

        # Creating An instance
        first_model = BaseModel()

        # checking if the id assigned on it is a string
        self.assertIsInstance(first_model.id, str)

        # Checking created_at and updated_at object
        self.assertIsInstance(first_model.created_at, datetime)
        self.assertIsInstance(first_model.updated_at, datetime)

    def test_unique_ids(self):
        # Test the uniqueness of Base_models instance's ids
        first_one = BaseModel()
        second_one = BaseModel()

        # Checking if the ids are different
        self.assertNotEqual(first_one.id, second_one.id)

    def test_save_method(self):
        model = BaseModel()
        initial_update_at = model.updated_at
        model.save()
        # Check if updated_at is updated after calling save
        self.assertNotEqual(initial_update_at, model.updated_at)

    def test_to_dict(self):
        # Create a BaseModel instance
        model = BaseModel()

        # Call the to_dict method
        result = model.to_dict()

        # Verify that the result is a dictionary
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
