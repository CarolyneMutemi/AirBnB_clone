#!/usr/bin/python3
"""
Has tests for the FileStorage class.
"""

import unittest
import json
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Tests the FileStorage class.
    """
    def setUp(self):
        self.new_model = BaseModel()

    def test_class_attributes(self):
        """
        Tests the class attributes.
        """
        self.assertEqual(storage.all(), FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_all(self):
        """
        Tests the all method.
        """
        self.assertIn(f"BaseModel.{self.new_model.id}", storage.all())
        self.assertIs(type(storage.all()), dict)

    def test_new(self):
        """
        Tests the new method.
        """
        derived_model = BaseModel(**(self.new_model.to_dict()))
        self.assertIn(f"BaseModel.{self.new_model.id}", storage.all())
        self.assertIn(f"BaseModel.{derived_model.id}", storage.all())
        # Since save and reload haven't been called
        # the object in storage.all() will be the new one.
        self.assertIs(storage.all()[f"BaseModel.{self.new_model.id}"],
                      self.new_model)
        self.assertIsNot(storage.all()[f"BaseModel.{derived_model.id}"],
                         derived_model)

    def test_save(self):
        """
        Tests the save method.
        """
        another_model = BaseModel()
        self.assertIs(storage.all()[f"BaseModel.{self.new_model.id}"],
                      self.new_model)
        self.assertIs(storage.all()[f"BaseModel.{another_model.id}"],
                      another_model)
        # If we call save in one of the models, both models will be saved
        # because the save function will save
        # the current state of storage.all().
        self.new_model.save()
        self.assertTrue(os.path.isfile('file.json'), True)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            another_model_key = f"BaseModel.{another_model.id}"
            new_model_key = f"BaseModel.{self.new_model.id}"
            self.assertIn(another_model_key, saved_objects)
            self.assertIn(new_model_key, saved_objects)
            self.assertEqual(saved_objects[another_model_key],
                             another_model.to_dict())
            self.assertEqual(saved_objects[new_model_key],
                             self.new_model.to_dict())

    def test_reload(self):
        """
        Tests the reload method.
        """
        try:
            if os.path.isfile('file.json') is False:
                storage.reload()
        except FileNotFoundError as error:
            self.assertTrue(error)

        new_model_key = f"BaseModel.{self.new_model.id}"
        self.new_model.save()
        reloaded_objects = storage.all()
        self.assertIs(reloaded_objects[new_model_key], self.new_model)
        storage.reload()
        self.assertIsNot(reloaded_objects[new_model_key], self.new_model)
        self.assertEqual(reloaded_objects[new_model_key].to_dict(),
                         self.new_model.to_dict())
