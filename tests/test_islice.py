import unittest
from itertools import islice

from iterable_collections import collect


class TestISlice(unittest.TestCase):

    def test_middle_list(self):
        c = collect([1, 2, 3, 4, 5, 6, 7, 8]).islice(4, 6)
        self.assertEqual(c.list(), list(islice([1, 2, 3, 4, 5, 6, 7, 8], 4, 6)))

    def test_beginning_list(self):
        c = collect([1, 2, 3, 4, 5, 6, 7, 8]).islice(4)
        self.assertEqual(c.list(), list(islice([1, 2, 3, 4, 5, 6, 7, 8], 4)))

    def test_end_list(self):
        c = collect([1, 2, 3, 4, 5, 6, 7, 8]).islice(4, None)
        self.assertEqual(c.list(), list(islice([1, 2, 3, 4, 5, 6, 7, 8], 4, None)))

    def test_middle_set(self):
        c = collect({1, 2, 3, 4, 5, 6, 7, 8}).islice(4, 6)
        self.assertEqual(c.set(), set(islice({1, 2, 3, 4, 5, 6, 7, 8}, 4, 6)))

    def test_beginning_set(self):
        c = collect({1, 2, 3, 4, 5, 6, 7, 8}).islice(4)
        self.assertEqual(c.set(), set(islice({1, 2, 3, 4, 5, 6, 7, 8}, 4)))

    def test_end_set(self):
        c = collect({1, 2, 3, 4, 5, 6, 7, 8}).islice(4, None)
        self.assertEqual(c.set(), set(islice({1, 2, 3, 4, 5, 6, 7, 8}, 4, None)))

    def test_middle_tuple(self):
        c = collect((1, 2, 3, 4, 5, 6, 7, 8)).islice(4, 6)
        self.assertEqual(c.tuple(), tuple(islice((1, 2, 3, 4, 5, 6, 7, 8), 4, 6)))

    def test_beginning_tuple(self):
        c = collect((1, 2, 3, 4, 5, 6, 7, 8)).islice(4)
        self.assertEqual(c.tuple(), tuple(islice((1, 2, 3, 4, 5, 6, 7, 8), 4)))

    def test_end_tuple(self):
        c = collect((1, 2, 3, 4, 5, 6, 7, 8)).islice(4, None)
        self.assertEqual(c.tuple(), tuple(islice((1, 2, 3, 4, 5, 6, 7, 8), 4, None)))

    def test_middle_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).islice(1, 3)
        with self.assertRaises(ValueError):
            c.dict()

    def test_beginning_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).islice(0, 2)
        with self.assertRaises(ValueError):
            c.dict()

    def test_end_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).islice(2)
        with self.assertRaises(ValueError):
            c.dict()
