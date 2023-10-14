#!/usr/bin/python3

"""
Has tests for the States class.
"""

import unittest
from models.state import State
import datetime
import json
from io import StringIO
from unittest.mock import patch
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
