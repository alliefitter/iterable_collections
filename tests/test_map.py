import unittest

from iterable_collections import collect


class TestMap(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).map(lambda x: x + 1)
        self.assertEqual(c.list(), list(map(lambda x: x + 1, list(range(10)))))

    def test_lists(self):
        c = collect(list(range(10))).map(lambda x: x + 1)
        self.assertEqual(c.list(), list(map(lambda x: x + 1, list(range(10)))))

    def test_set(self):
        c = collect(set(range(10))).map(lambda x: x + 1)
        self.assertEqual(c.set(), set(map(lambda x: x + 1, list(range(10)))))

    def test_tuple(self):
        c = collect(tuple(range(10))).map(lambda x: x + 1)
        self.assertEqual(c.tuple(), tuple(map(lambda x: x + 1, list(range(10)))))

    def test_iterator(self):
        c = collect(iter(range(10))).map(lambda x: x + 1)
        self.assertEqual(c.list(), list(map(lambda x: x + 1, list(range(10)))))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).map(lambda x: x + 'b')
        self.assertEqual(c.list(), list(map(lambda x: x + 'b', {'a': 1, 'b': 2})))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).map(lambda x: x[1] + 1)
        self.assertEqual(c.list(), list(map(lambda x: x[1] + 1, {'a': 1, 'b': 2}.items())))
