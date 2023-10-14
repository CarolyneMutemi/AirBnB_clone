#!/usr/bin/python3

"""
Has tests for the States class.
"""

import unittest
import datetime
import json
from io import StringIO
from unittest.mock import patch
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """
    Tests for the State class and attributes.
    """
    def setUp(self):
        self.my_state = State()
        self.my_state_key = f"State.{self.my_state.id}"

    def test_public_class_attributes(self):
        """
        Tests the public class attributes.
        """
        self.assertIs(State.name, "")
        self.assertNotIn('name', self.my_state.__dict__)
        self.my_state.name = 'Nairobi'
        self.assertIs(self.my_state.name, "Nairobi")
        self.assertIn('name', self.my_state.__dict__)
        self.my_state.name = ['Makueni', 'Coast', 'Kisumu']
        self.assertEqual(self.my_state.name, ['Makueni', 'Coast', 'Kisumu'])
        self.my_state.name = 12
        self.assertIs(self.my_state.name, 12)
        self.my_state.name = {'state': 'Nairobi'}
        self.assertEqual(self.my_state.name, {'state': 'Nairobi'})
        self.my_state.name = True
        self.assertIs(self.my_state.name, True)
        self.my_state.name = {'Kitui'}
        self.assertEqual(self.my_state.name, {'Kitui'})
        self.my_state.name = ('Rift Valley', 'Kisii')
        self.assertEqual(self.my_state.name, ('Rift Valley', 'Kisii'))

    def test_init(self):
        """
        Tests the init method.
        """
        self.assertIs(self.my_state.__class__.__name__, 'State')
        self.assertIn('created_at', self.my_state.__dict__)
        self.assertIn('updated_at', self.my_state.__dict__)
        self.assertIn('id', self.my_state.__dict__)
        self.assertIs(type(self.my_state.__dict__['id']), str)
        self.assertIs(type(self.my_state.__dict__['created_at']),
                      datetime.datetime)
        self.assertIs(type(self.my_state.__dict__['updated_at']),
                      datetime.datetime)

    def test_str(self):
        """
        Tests the str method.
        """
        str_text1 = f"[{self.my_state.__class__.__name__}] "
        str_text2 = f"({self.my_state.id}) {self.my_state.__dict__}\n"
        str_text = str_text1 + str_text2
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(self.my_state)
            self.assertEqual(mock_print.getvalue(), str_text)

    def test_save(self):
        """
        Tests the save method.
        """
        first_update = self.my_state.updated_at
        self.assertIn(self.my_state_key, storage.all())
        self.assertIs(storage.all()[self.my_state_key], self.my_state)
        self.my_state.save()
        self.assertNotEqual(first_update, self.my_state.updated_at)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            self.assertIn(self.my_state_key, saved_objects)
        storage.reload()
        self.assertIsNot(storage.all()[self.my_state_key], self.my_state)
        self.assertEqual(storage.all()[self.my_state_key].to_dict(),
                         self.my_state.to_dict())

    def test_to_dict(self):
        """
        Tests the to_dict method.
        """
        self.assertNotEqual(self.my_state.__dict__,
                            self.my_state.to_dict())
        self.assertIn('__class__', self.my_state.to_dict())
        self.assertNotIn('__class__', self.my_state.__dict__)
        self.assertIs(type(self.my_state.to_dict()['created_at']), str)
        self.assertIs(type(self.my_state.to_dict()['updated_at']), str)
