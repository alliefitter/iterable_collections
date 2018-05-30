import unittest

from iterable_collections import collect


class TestFilter(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).filter(lambda x: x < 5)
        self.assertEqual(c.list(), list(filter(lambda x: x < 5, list(range(10)))))

    def test_set(self):
        c = collect(set(range(10))).filter(lambda x: x < 5)
        self.assertEqual(c.set(), set(filter(lambda x: x < 5, list(range(10)))))

    def test_tuple(self):
        c = collect(tuple(range(10))).filter(lambda x: x < 5)
        self.assertEqual(c.tuple(), tuple(filter(lambda x: x < 5, list(range(10)))))

    def test_iterator(self):
        c = collect(iter(range(10))).filter(lambda x: x < 5)
        self.assertEqual(c.list(), list(filter(lambda x: x < 5, list(range(10)))))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).filter(lambda x: x < 'b')
        self.assertEqual(c.list(), list(filter(lambda x: x < 'b', {'a': 1, 'b': 2})))
