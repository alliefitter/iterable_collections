import unittest

from iterable_collections import collect


class TestLen(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        self.assertEqual(c.len(), len(list(range(10))))

    def test_set(self):
        c = collect(set(range(10)))
        self.assertEqual(c.len(), len(set(range(10))))

    def test_tuple(self):
        c = collect(tuple(range(10)))
        self.assertEqual(c.len(), len(tuple(range(10))))

    def test_iterator(self):
        c = collect(iter(range(10))).list_()
        self.assertEqual(c.len(), len(list(iter(range(10)))))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.len(), len(list({'a': 1, 'b': 2})))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(c.len(), len({'a': 1, 'b': 2}.items()))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate().list_()
        self.assertEqual(c.len(), len(list(enumerate(range(10)))))
