import unittest

from iterable_collections import collect


class TestNext(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        i = iter(list(range(10)))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))

    def test_set(self):
        c = collect(set(range(10)))
        i = iter(set(range(10)))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))

    def test_tuple(self):
        c = collect(tuple(range(10)))
        i = iter(tuple(range(10)))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))

    def test_iterator(self):
        c = collect(iter(range(10)))
        i = iter(iter(range(10)))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        i = iter({'a': 1, 'b': 2})
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        i = iter({'a': 1, 'b': 2}.items())
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate()
        i = iter(enumerate(range(10)))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))
        self.assertEqual(c.next(), next(i))

