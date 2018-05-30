import unittest

from iterable_collections import collect


class TestList_(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).list_()
        self.assertEqual(c.iterable, list(list(range(10))))

    def test_set(self):
        c = collect(set(range(10))).list_()
        self.assertEqual(c.iterable, list(set(range(10))))

    def test_tuple(self):
        c = collect(tuple(range(10))).list_()
        self.assertEqual(c.iterable, list(tuple(range(10))))

    def test_iterator(self):
        c = collect(iter(range(10))).list_()
        self.assertEqual(c.iterable, list(iter(range(10))))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).list_()
        self.assertEqual(c.iterable, list({'a': 1, 'b': 2}))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).list_()
        self.assertEqual(c.iterable, list({'a': 1, 'b': 2}.items()))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate().list_()
        self.assertEqual(c.iterable, list(enumerate(range(10))))

