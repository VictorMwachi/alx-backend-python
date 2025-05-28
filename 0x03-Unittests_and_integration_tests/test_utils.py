#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ("test",{"a": 1}, ("a",),1),
        ("test2",{"a": {"b": 2}}, ("a",),{"b":2}),
        ("test3",{"a": {"b": 2}}, ("a", "b"),2)
    ])
    def test_access_nested_map(self,name,nested_map,path,expected):
        self.assertEqual(access_nested_map(nested_map, path),expected)