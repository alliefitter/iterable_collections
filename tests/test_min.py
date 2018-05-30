import unittest

from iterable_collections import collect


class TestMin(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        self.assertEqual(c.min(), min(list(range(10))))

    def test_set(self):
        c = collect(set(range(10)))
        self.assertEqual(c.min(), min(set(range(10))))

    def test_tuple(self):
        c = collect(tuple(range(10)))
        self.assertEqual(c.min(), min(tuple(range(10))))

    def test_iterator(self):
        c = collect(iter(range(10))).list_()
        self.assertEqual(c.min(), min(list(iter(range(10)))))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.min(), min(list({'a': 1, 'b': 2})))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(c.min(), min({'a': 1, 'b': 2}.items()))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate().list_()
        self.assertEqual(c.min(), min(list(enumerate(range(10)))))
