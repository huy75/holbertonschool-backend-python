#!/usr/bin/env python3
""" Unittest module """
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Test method returns correct output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)
