#!/usr/bin/env python3
"""
Tests the utils.access_nested_map function.
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               expected_result: Union[int, Mapping]) -> None:
        """ Test access_nested_map returns expected ouput """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected_message: str) -> None:
        """ Test access_nested_map raises exception for invalid inputs """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check that exception message matches the expected message
        self.assertEqual(str(context.exception), expected_message)
