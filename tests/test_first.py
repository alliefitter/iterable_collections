import unittest
from operator import itemgetter

from iterable_collections import collect


class TestFirst(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        self.assertEqual(c.first(), itemgetter(0)(list(range(10))))

    def test_empty_list(self):
        c = collect(list())
        with self.assertRaises(IndexError):
            c.first()

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(TypeError):
            c.first()

    def test_tuple(self):
        c = collect(tuple(range(10)))
        self.assertEqual(c.first(), itemgetter(0)(list(range(10))))

    def test_empty_tuple(self):
        c = collect(tuple())
        with self.assertRaises(IndexError):
            c.first()

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(TypeError):
            c.first()

    def test_dict(self):
        c = collect({0: 1, 2: 2})
        self.assertEqual(c.first(), itemgetter(0)({0: 1, 2: 2}))

    def test_dict_with_error(self):
        c = collect({'a': 1, 'b': 2})
        with self.assertRaises(KeyError):
            c.first()

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        with self.assertRaises(TypeError):
            c.first()

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate()
        with self.assertRaises(TypeError):
            c.first()

