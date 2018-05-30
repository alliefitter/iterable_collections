import unittest

from iterable_collections import collect
from iterable_collections.utils import make_nt_items


class TestFilterNtItems(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.filter_nt_items(lambda i: i.value < 2)

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.filter_nt_items(lambda i: i.value < 2)

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.filter_nt_items(lambda i: i.value < 2)

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.filter_nt_items(lambda i: i.value < 2)

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).filter_nt_items(lambda i: i.value < 2)
        self.assertEqual(
            c.dict(),
            dict(filter(lambda i: i.value < 2, make_nt_items({'a': 1, 'b': 2}.items())))
        )

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).filter_nt_items(lambda i: i.value < 2)
        self.assertEqual(
            c.dict(),
            dict(filter(lambda i: i.value < 2, make_nt_items(dict({'a': 1, 'b': 2}.items()).items())))
        )
