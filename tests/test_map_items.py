import unittest

from iterable_collections import collect
from iterable_collections.utils import spread_tuple_parameter


class TestMapItems(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.map_items(lambda k, v: (k, v + 1))

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.map_items(lambda k, v: (k, v + 1))

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.map_items(lambda k, v: (k, v + 1))

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.map_items(lambda k, v: (k, v + 1))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).map_items(lambda k, v: (k, v + 1))
        self.assertEqual(c.dict(), dict(map(*spread_tuple_parameter(lambda k, v: (k, v + 1)), {'a': 1, 'b': 2}.items())))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).map_items(lambda k, v: (k, v + 1))
        self.assertEqual(
            c.dict(),
            dict(map(*spread_tuple_parameter(lambda k, v: (k, v + 1)), dict({'a': 1, 'b': 2}.items()).items()))
        )
