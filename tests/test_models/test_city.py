#!/usr/bin/python3

"""
Has tests for the City class.
"""

import unittest
import datetime
import json
from io import StringIO
from unittest.mock import patch
from models.city import City
from models.state import State
from models import storage


class TestCity(unittest.TestCase):
    """
    Tests for the City class and its attributes.
    """

    def setUp(self):
        self.my_state = State()
        self.my_city = City()
        self.my_city_key = f"City.{self.my_city.id}"

    def test_public_class_attributes(self):
        """
        Tests the public class attributes.
        """
        self.assertIs(City.name, "")
        self.assertIs(City.state_id, "")
        self.assertNotIn('name', self.my_city.__dict__)
        self.assertNotIn('state_id', self.my_city.__dict__)
        self.my_city.name = 'Nairobi'
        self.my_city.state_id = self.my_state.id
        self.assertIs(self.my_city.name, 'Nairobi')
        self.assertIs(self.my_city.state_id, self.my_state.id)
        self.my_city.name = 12
        self.my_city.state_id = 12
        self.assertIs(self.my_city.name, 12)
        self.assertIs(self.my_city.state_id, 12)
        self.my_city.name = {'Lodwar'}
        self.my_city.state_id = {'123'}
        self.assertEqual(self.my_city.name, {'Lodwar'})
        self.assertEqual(self.my_city.state_id, {'123'})
        self.my_city.name = ['Turkana']
        self.my_city.state_id = [98]
        self.assertEqual(self.my_city.name, ['Turkana'])
        self.assertEqual(self.my_city.state_id, [98])
        self.my_city.name = {'name': 'Kibwezi'}
        self.my_city.state_id = {'id': 678}
        self.assertEqual(self.my_city.name, {'name': 'Kibwezi'})
        self.assertEqual(self.my_city.state_id, {'id': 678})
        self.my_city.name = True
        self.my_city.state_id = False
        self.assertIs(self.my_city.name, True)
        self.assertIs(self.my_city.state_id, False)

    def test_init(self):
        """
        Tests the init method.
        """
        self.assertIs(self.my_city.__class__.__name__, 'City')
        self.assertIn('created_at', self.my_city.__dict__)
        self.assertIn('updated_at', self.my_city.__dict__)
        self.assertIn('id', self.my_city.__dict__)
        self.assertIs(type(self.my_city.__dict__['id']), str)
        self.assertIs(type(self.my_city.__dict__['created_at']),
                      datetime.datetime)
        self.assertIs(type(self.my_city.__dict__['updated_at']),
                      datetime.datetime)

    def test_str(self):
        """
        Tests the str method.
        """
        str_text1 = f"[{self.my_city.__class__.__name__}] "
        str_text2 = f"({self.my_city.id}) {self.my_city.__dict__}\n"
        str_text = str_text1 + str_text2
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(self.my_city)
            self.assertEqual(mock_print.getvalue(), str_text)

    def test_save(self):
        """
        Tests the save method.
        """
        first_update = self.my_city.updated_at
        self.assertIn(self.my_city_key, storage.all())
        self.assertIs(storage.all()[self.my_city_key], self.my_city)
        self.my_city.save()
        self.assertNotEqual(first_update, self.my_city.updated_at)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            self.assertIn(self.my_city_key, saved_objects)
        storage.reload()
        self.assertIsNot(storage.all()[self.my_city_key], self.my_city)
        self.assertEqual(storage.all()[self.my_city_key].to_dict(),
                         self.my_city.to_dict())

    def test_to_dict(self):
        """
        Tests the to_dict method.
        """
        self.assertNotEqual(self.my_city.__dict__,
                            self.my_city.to_dict())
        self.assertIn('__class__', self.my_city.to_dict())
        self.assertNotIn('__class__', self.my_city.__dict__)
        self.assertIs(type(self.my_city.to_dict()['created_at']), str)
        self.assertIs(type(self.my_city.to_dict()['updated_at']), str)
