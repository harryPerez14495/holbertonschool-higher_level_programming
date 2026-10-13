#!/usr/bin/python3
"""Unit tests for the max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for finding the maximum integer."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 8, 3, 2]), 8)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 3.7, 2.1]), 3.7)

    def test_mixed_floats_integers(self):
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_large_numbers(self):
        self.assertEqual(max_integer([100, 9999, 500]), 9999)

    def test_two_elements(self):
        self.assertEqual(max_integer([2, 1]), 2)

    def test_negative_single(self):
        self.assertEqual(max_integer([-7]), -7)

    def test_default_argument(self):
        self.assertIsNone(max_integer())

    def test_strings(self):
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_tuple(self):
        self.assertEqual(max_integer((1, 5, 3)), 5)
