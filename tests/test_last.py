import unittest
from operator import itemgetter

from iterable_collections import collect


class TestLast(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        self.assertEqual(c.last(), itemgetter(-1)(list(range(10))))

    def test_empty_list(self):
        c = collect(list())
        with self.assertRaises(IndexError):
            c.last()

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(TypeError):
            c.last()

    def test_tuple(self):
        c = collect(tuple(range(10)))
        self.assertEqual(c.last(), itemgetter(-1)(list(range(10))))

    def test_empty_tuple(self):
        c = collect(tuple())
        with self.assertRaises(IndexError):
            c.last()

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(TypeError):
            c.last()

    def test_dict(self):
        c = collect({-1: 1, 0: 2})
        print(c.last())
        self.assertEqual(c.last(), itemgetter(-1)({-1: 1, 0: 2}))

    def test_dict_with_error(self):
        c = collect({'a': 1, 'b': 2})
        with self.assertRaises(KeyError):
            c.last()

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        with self.assertRaises(TypeError):
            c.last()

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate()
        with self.assertRaises(TypeError):
            c.last()

