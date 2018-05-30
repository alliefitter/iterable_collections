import unittest

from iterable_collections import collect


class TestContains(unittest.TestCase):

    def test_list(self):
        c = collect([1, 2, 3, 4, 5])
        self.assertTrue(c.contains(1))
        self.assertFalse(c.contains('a'))

    def test_set(self):
        c = collect({1, 2, 3, 4, 5})
        self.assertTrue(c.contains(1))
        self.assertFalse(c.contains('a'))

    def test_tuple(self):
        c = collect({1, 2, 3, 4, 5})
        self.assertTrue(c.contains(1))
        self.assertFalse(c.contains('a'))

    def test_iter(self):
        c = collect(iter([1, 2, 3, 4, 5]))
        self.assertTrue(c.contains(1))
        self.assertFalse(c.contains('a'))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertFalse(c.contains(1))
        self.assertTrue(c.contains('a'))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertFalse(c.contains(1))
        self.assertFalse(c.contains('a'))
        self.assertTrue(c.contains(('a', 1)))

    def test_enumerate(self):
        c = collect([1, 2, 3, 4, 5]).enumerate().list_()
        self.assertFalse(c.contains(1))
        self.assertFalse(c.contains('a'))
        self.assertTrue(c.list_().contains((0, 1)))
