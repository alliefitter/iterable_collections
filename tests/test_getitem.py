import unittest
from operator import getitem

from iterable_collections import collect


class TestGetitem(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        self.assertEqual(c.getitem(2), getitem(list(range(10)), 2))

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(TypeError):
            c.getitem(2)

    def test_tuple(self):
        c = collect(tuple(range(10)))
        self.assertEqual(c.getitem(2), getitem(tuple(range(10)), 2))

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(TypeError):
            c.getitem(2)

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.getitem('a'), getitem({'a': 1, 'b': 2}, 'a'))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        with self.assertRaises(TypeError):
            c.getitem(2)

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate()
        with self.assertRaises(TypeError):
            c.getitem(2)

