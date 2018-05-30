import unittest
from collections import OrderedDict

from iterable_collections import collect


class TestOrderedDict(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.ordered_dict()

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.ordered_dict()

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.ordered_dict()

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.ordered_dict()

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.ordered_dict(), OrderedDict({'a': 1, 'b': 2}))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(c.ordered_dict(), OrderedDict({'a': 1, 'b': 2}.items()))

    def test_list_of_tuples(self):
        c = collect([('a', 1), ('b', 2), ('c', 3)])
        self.assertEqual(c.ordered_dict(), OrderedDict([('a', 1), ('b', 2), ('c', 3)]))

    def test_zip(self):
        c = collect(['a', 'b', 'c']).zip([1, 2, 3])
        self.assertEqual(c.ordered_dict(), dict(zip(['a', 'b', 'c'], [1, 2, 3])))
