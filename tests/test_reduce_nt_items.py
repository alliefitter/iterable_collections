import unittest
from functools import reduce

from iterable_collections import collect
from iterable_collections.utils import make_nt_items


class TestReduceNtItems(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.reduce_nt_items(lambda c_, i: i.value + c_, 0)

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.reduce_nt_items(lambda c_, i: i.value + c_, 0)

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.reduce_nt_items(lambda c_, i: i.value + c_, 0)

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.reduce_nt_items(lambda c_, i: i.value + c_, 0)

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(
            c.reduce_nt_items(lambda c_, i: i.value + c_, 0),
            reduce(lambda c_, i: i.value + c_, make_nt_items({'a': 1, 'b': 2}.items()), 0)
        )

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(
            c.reduce_nt_items(lambda c_, i: i.value + c_, 0),
            reduce(lambda c_, i: i.value + c_, make_nt_items(dict({'a': 1, 'b': 2}.items()).items()), 0)
        )
