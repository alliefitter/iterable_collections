import unittest
from functools import reduce

from iterable_collections import collect
from iterable_collections.utils import spread_tuple_parameter


class TestReduceItems(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.reduce_items(lambda c_, k, v: v + c_, 0)

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.reduce_items(lambda c_, k, v: v + c_, 0)

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.reduce_items(lambda c_, k, v: v + c_, 0)

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.reduce_items(lambda c_, k, v: v + c_, 0)

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(
            c.reduce_items(lambda c_, k, v: v + c_, 0),
            reduce(*spread_tuple_parameter(lambda c_, k, v: v + c_, pos=1), {'a': 1, 'b': 2}.items(), 0)
        )

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(
            c.reduce_items(lambda c_, k, v: v + c_, 0),
            reduce(*spread_tuple_parameter(lambda c_, k, v: v + c_, pos=1), dict({'a': 1, 'b': 2}.items()).items(), 0)
        )
