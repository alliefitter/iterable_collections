import unittest

from iterable_collections import collect


class TestZip(unittest.TestCase):

    def test_strs(self):
        c = collect('abcdefghi').zip('foobarbaz')
        self.assertEqual(c.list(), list(zip('abcdefghi', 'foobarbaz')))

    def test_lists(self):
        c = collect(list(range(10))).zip(list(range(10, 0, -1)))
        self.assertEqual(c.list(), list(zip(list(range(10)), list(range(10, 0, -1)))))

    def test_sets(self):
        c = collect(set(range(10))).zip(set(range(10, 0, -1)))
        self.assertEqual(c.list(), list(zip(set(range(10)), set(range(10, 0, -1)))))

    def test_tuples(self):
        c = collect(tuple(range(10))).zip(tuple(range(10, 0, -1)))
        self.assertEqual(c.list(), list(zip(tuple(range(10)), tuple(range(10, 0, -1)))))

    def test_iters(self):
        c = collect(iter(range(10))).zip(iter(range(10, 0, -1)))
        self.assertEqual(c.list(), list(zip(iter(range(10)), iter(range(10, 0, -1)))))

    def test_dicts(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).zip({'d': 4, 'e': 5, 'f': 6})
        self.assertEqual(c.list(), list(zip({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6})))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}.items()).zip({'d': 4, 'e': 5, 'f': 6}.items())
        self.assertEqual(c.list(), list(zip({'a': 1, 'b': 2, 'c': 3}.items(), {'d': 4, 'e': 5, 'f': 6}.items())))
