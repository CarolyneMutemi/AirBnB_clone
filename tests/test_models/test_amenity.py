#!/usr/bin/python3

"""
Has tests for the amenity class
"""

import unittest
import datetime
import json
from io import StringIO
from unittest.mock import patch
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """
    Tests the Amenity class and its attributes.
    """

    def setUp(self):
        self.amenity = Amenity()
        self.amenity_key = f"Amenity.{self.amenity.id}"

    def test_public_class_attributes(self):
        """
        Tests the public class attributes.
        """
        self.assertIs(Amenity.name, "")
        self.assertNotIn('name', self.amenity.__dict__)
        self.amenity.name = "Private Beach"
        self.assertIs(self.amenity.name, 'Private Beach')
        self.amenity.name = 12
        self.assertIs(self.amenity.name, 12)
        self.amenity.name = ["Private Beach"]
        self.assertEqual(self.amenity.name, ['Private Beach'])
        self.amenity.name = {"Private Beach"}
        self.assertEqual(self.amenity.name, {'Private Beach'})
        self.amenity.name = ("Private Beach", "Fun Park")
        self.assertEqual(self.amenity.name, ('Private Beach', "Fun Park"))
        self.amenity.name = {'name': "Private Beach"}
        self.assertEqual(self.amenity.name, {'name': 'Private Beach'})
        self.amenity.name = True
        self.assertIs(self.amenity.name, True)

    def test_init(self):
        """
        Tests the init method.
        """
        self.assertIs(self.amenity.__class__.__name__, 'Amenity')
        self.assertIn('created_at', self.amenity.__dict__)
        self.assertIn('updated_at', self.amenity.__dict__)
        self.assertIn('id', self.amenity.__dict__)
        self.assertIs(type(self.amenity.__dict__['id']), str)
        self.assertIs(type(self.amenity.__dict__['created_at']),
                      datetime.datetime)
        self.assertIs(type(self.amenity.__dict__['updated_at']),
                      datetime.datetime)

    def test_str(self):
        """
        Tests the str method.
        """
        str_text1 = f"[{self.amenity.__class__.__name__}] "
        str_text2 = f"({self.amenity.id}) {self.amenity.__dict__}\n"
        str_text = str_text1 + str_text2
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(self.amenity)
            self.assertEqual(mock_print.getvalue(), str_text)

    def test_save(self):
        """
        Tests the save method.
        """
        first_update = self.amenity.updated_at
        self.assertIn(self.amenity_key, storage.all())
        self.assertIs(storage.all()[self.amenity_key], self.amenity)
        self.amenity.save()
        self.assertNotEqual(first_update, self.amenity.updated_at)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            self.assertIn(self.amenity_key, saved_objects)
        storage.reload()
        self.assertIsNot(storage.all()[self.amenity_key], self.amenity)
        self.assertEqual(storage.all()[self.amenity_key].to_dict(),
                         self.amenity.to_dict())

    def test_to_dict(self):
        """
        Tests the to_dict method.
        """
        self.assertNotEqual(self.amenity.__dict__,
                            self.amenity.to_dict())
        self.assertIn('__class__', self.amenity.to_dict())
        self.assertNotIn('__class__', self.amenity.__dict__)
        self.assertIs(type(self.amenity.to_dict()['created_at']), str)
        self.assertIs(type(self.amenity.to_dict()['updated_at']), str)
