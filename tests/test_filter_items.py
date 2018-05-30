import unittest

from iterable_collections import collect
from iterable_collections.utils import spread_tuple_parameter


class TestFilterItems(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.filter_items(lambda k, v: v < 2)

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.filter_items(lambda k, v: v < 2)

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.filter_items(lambda k, v: v < 2)

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.filter_items(lambda k, v: v < 2)

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).filter_items(lambda k, v: v < 2)
        self.assertEqual(c.dict(), dict(filter(*spread_tuple_parameter(lambda k, v: v < 2), {'a': 1, 'b': 2}.items())))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).filter_items(lambda k, v: v < 2)
        self.assertEqual(
            c.dict(),
            dict(filter(*spread_tuple_parameter(lambda k, v: v < 2), dict({'a': 1, 'b': 2}.items()).items()))
        )
