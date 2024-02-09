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

if __name__ == '__main__':
	unittest.main()
