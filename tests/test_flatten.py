import unittest
from itertools import chain

from iterable_collections import collect


class TestFlatten(unittest.TestCase):

    def test_nested_list(self):
        c = collect([[1, 2], ['foo', 4], [5, b'bar'], [7, 8]]).flatten()
        self.assertEqual(c.iterable, [1, 2, 'foo', 4, 5, b'bar', 7, 8])

    def test_nested_tuple(self):
        c = collect(((1, 2), ('foo', 4), (5, b'bar'), (7, 8))).flatten()
        self.assertEqual(c.iterable, [1, 2, 'foo', 4, 5, b'bar', 7, 8])

    def test_nested_iter(self):
        c = collect(chain(iter((1, 2)), iter(('foo', 4)), iter((5, b'bar')), iter((7, 8)))).flatten()
        self.assertEqual(c.iterable, [1, 2, 'foo', 4, 5, b'bar', 7, 8])

    def test_deeply_nested_list(self):
        c = collect([[1, [2, ['foo', 4]], [[5], [b'bar', [7, [8]]]]]]).flatten()
        self.assertEqual(c.iterable, [1, 2, 'foo', 4, 5, b'bar', 7, 8])
