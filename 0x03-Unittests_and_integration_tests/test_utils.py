#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ("test",{"a": 1}, ("a",)),
        ("test2",{"a": {"b": 2}}, ("a",)),
        ("test3",{"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self,name,nested_map,path):
        self.assertEqual(access_nested_map(nested_map={"a": 1}, path=("a",)),1)