import unittest
from functools import reduce

from iterable_collections import collect


class TestReduce(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        self.assertEqual(c.reduce(lambda c_, x: x + c_, 0), reduce(lambda c_, x: x + c_, list(range(10)), 0))

    def test_set(self):
        c = collect(set(range(10)))
        self.assertEqual(c.reduce(lambda c_, x: x + c_, 0), reduce(lambda c_, x: x + c_, list(range(10)), 0))

    def test_tuple(self):
        c = collect(tuple(range(10)))
        self.assertEqual(c.reduce(lambda c_, x: x + c_, 0), reduce(lambda c_, x: x + c_, list(range(10)), 0))

    def test_iterator(self):
        c = collect(iter(range(10)))
        self.assertEqual(c.reduce(lambda c_, x: x + c_, 0), reduce(lambda c_, x: x + c_, list(range(10)), 0))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.reduce(lambda c_, x: x + c_, 'z'), reduce(lambda c_, x: x + c_, {'a': 1, 'b': 2}, 'z'))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(
            c.reduce(lambda c_, x: x[1] + c_, 0),
            reduce(lambda c_, x: x[1] + c_, {'a': 1, 'b': 2}.items(), 0)
        )
