import unittest

from iterable_collections import collect


class TestChunks(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        c.chunks(2)
        self.assertEqual([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]], c.iterable)

    def test_set(self):
        c = collect(set(range(10)))
        c.chunks(2)
        self.assertEqual([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]], c.iterable)

    def test_tuple(self):
        c = collect(tuple(range(10)))
        c.chunks(2)
        self.assertEqual([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]], c.iterable)

    def test_iterator(self):
        c = collect(iter(range(10)))
        c.chunks(2)
        self.assertEqual([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]], c.iterable)

    def test_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4})
        c.chunks(2)
        self.assertEqual(c.iterable, [[('a', 1), ('b', 2)], [('c', 3), ('d', 4)]])

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}.items())
        c.chunks(2)
        self.assertEqual(c.iterable, [[('a', 1), ('b', 2)], [('c', 3), ('d', 4)]])
