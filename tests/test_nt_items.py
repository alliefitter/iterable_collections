import unittest

from iterable_collections import collect
from iterable_collections.utils import DictItem


class TestNTItems(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.nt_items()

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.nt_items()

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.nt_items()

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.nt_items()

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).nt_items()
        self.assertEqual(c.iterable, list(map(DictItem._make, dict({'a': 1, 'b': 2}).items())))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).nt_items()
        self.assertEqual(c.iterable, list(map(DictItem._make, (dict({'a': 1, 'b': 2}.items()).items()))))

    def test_list_of_tuples(self):
        c = collect([('a', 1), ('b', 2), ('c', 3)]).nt_items()
        self.assertEqual(c.iterable, list(map(DictItem._make, (dict([('a', 1), ('b', 2), ('c', 3)]).items()))))

    def test_zip(self):
        c = collect(['a', 'b', 'c']).zip([1, 2, 3]).nt_items()
        self.assertEqual(c.iterable, list(map(DictItem._make, (dict(zip(['a', 'b', 'c'], [1, 2, 3])).items()))))
