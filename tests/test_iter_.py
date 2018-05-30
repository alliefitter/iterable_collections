import unittest

from iterable_collections import collect


class TestIter_(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).iter_()
        self.assertEqual(list(c.iterable), list(iter(list(range(10)))))

    def test_set(self):
        c = collect(set(range(10))).iter_()
        self.assertEqual(list(c.iterable), list(iter(set(range(10)))))

    def test_tuple(self):
        c = collect(tuple(range(10))).iter_()
        self.assertEqual(list(c.iterable), list(iter(tuple(range(10)))))

    def test_iterator(self):
        c = collect(iter(range(10))).iter_()
        self.assertEqual(list(c.iterable), list(iter(iter(range(10)))))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).iter_()
        self.assertEqual(list(c.iterable), list(iter({'a': 1, 'b': 2})))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).iter_()
        self.assertEqual(list(c.iterable), list(iter({'a': 1, 'b': 2}.items())))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate().iter_()
        self.assertEqual(list(c.iterable), list(iter(enumerate(range(10)))))

