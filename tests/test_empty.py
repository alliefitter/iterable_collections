import unittest

from iterable_collections import collect


class TestEmpty(unittest.TestCase):

    def test_list_true(self):
        c = collect(list())
        self.assertTrue(c.empty())

    def test_list_false(self):
        c = collect(list(range(10)))
        self.assertFalse(c.empty())

    def test_set_true(self):
        c = collect(set())
        self.assertTrue(c.empty())

    def test_set_false(self):
        c = collect(set(range(10)))
        self.assertFalse(c.empty())

    def test_tuple_true(self):
        c = collect(tuple())
        self.assertTrue(c.empty())

    def test_tuple_false(self):
        c = collect(tuple(range(10)))
        self.assertFalse(c.empty())

    def test_iter_true(self):
        c = collect(iter([]))
        self.assertTrue(c.empty())

    def test_iter_false(self):
        c = collect(iter(range(10)))
        self.assertFalse(c.empty())

    def test_dict_true(self):
        c = collect(dict())
        self.assertTrue(c.empty())

    def test_dict_false(self):
        c = collect(dict(a=1, b=2, c=3))
        self.assertFalse(c.empty())

    def test_dict_items_true(self):
        c = collect(dict().items())
        self.assertTrue(c.empty())

    def test_dict_items_false(self):
        c = collect(dict(a=1, b=2, c=3).items())
        self.assertFalse(c.empty())

