import unittest

from iterable_collections import collect


class TestTuple_(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).tuple_()
        self.assertEqual(c.iterable, tuple(range(10)))

    def test_set(self):
        c = collect(set(range(10))).tuple_()
        self.assertEqual(c.iterable, tuple(range(10)))

    def test_tuple(self):
        c = collect(tuple(range(10))).tuple_()
        self.assertEqual(c.iterable, tuple(range(10)))

    def test_iterator(self):
        c = collect(iter(range(10))).tuple_()
        self.assertEqual(c.iterable, tuple(range(10)))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).tuple_()
        self.assertEqual(c.iterable, tuple({'a': 1, 'b': 2}))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).tuple_()
        self.assertEqual(c.iterable, tuple({'a': 1, 'b': 2}.items()))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate().tuple_()
        self.assertEqual(c.iterable, tuple(enumerate(range(10))))
