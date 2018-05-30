import unittest

from iterable_collections import collect


class TestItems(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.items()

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.items()

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.items()

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.items()

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).items()
        self.assertEqual(c.iterable, dict({'a': 1, 'b': 2}).items())

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).items()
        self.assertEqual(c.iterable, dict({'a': 1, 'b': 2}.items()).items())

    def test_list_of_tuples(self):
        c = collect([('a', 1), ('b', 2), ('c', 3)]).items()
        self.assertEqual(c.iterable, dict([('a', 1), ('b', 2), ('c', 3)]).items())

    def test_zip(self):
        c = collect(['a', 'b', 'c']).zip([1, 2, 3]).items()
        self.assertEqual(c.iterable, dict(zip(['a', 'b', 'c'], [1, 2, 3])).items())
