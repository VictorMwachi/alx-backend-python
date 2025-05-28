#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Cases for access_nested_map function
    """
    @parameterized.expand([
        ("test1", {"a": 1}, ("a",), 1),
        ("test2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("test3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ("Empty Dictionary", {}, ("a",)),
        ("Missing Key", {"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, name, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
