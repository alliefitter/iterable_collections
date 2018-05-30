import unittest
from operator import setitem

from iterable_collections import collect


class TestSetitem(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).setitem(2, 0)
        t = list(range(10))
        setitem(t, 2, 0)
        self.assertEqual(c.iterable, t)

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(TypeError):
            c.setitem(2, 0)

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(TypeError):
            c.setitem(2, 0)

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(TypeError):
            c.setitem(2, 0)

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).setitem('a', 0)
        t = {'a': 1, 'b': 2}
        setitem(t, 'a', 0)
        self.assertEqual(c.iterable, t)

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        with self.assertRaises(TypeError):
            c.setitem(2, 0)

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate()
        with self.assertRaises(TypeError):
            c.setitem(2, 0)

