import unittest
from operator import itemgetter

from iterable_collections import collect


class TestLastItem(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.last_item()

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.last_item()

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.last_item()

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.last_item()

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.last_item(), itemgetter(-1)(list({'a': 1, 'b': 2}.items())))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(c.last_item(), itemgetter(-1)(list(dict({'a': 1, 'b': 2}.items()).items())))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate()
        self.assertEqual(c.last_item(), itemgetter(-1)(list(dict(enumerate(list(range(10)))).items())))
