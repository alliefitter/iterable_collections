import unittest

from iterable_collections import collect


class TestDict(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.dict()

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.dict()

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.dict()

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.dict()

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.dict(), dict({'a': 1, 'b': 2}))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(c.dict(), dict({'a': 1, 'b': 2}.items()))

    def test_list_of_tuples(self):
        c = collect([('a', 1), ('b', 2), ('c', 3)])
        self.assertEqual(c.dict(), dict([('a', 1), ('b', 2), ('c', 3)]))

    def test_zip(self):
        c = collect(['a', 'b', 'c']).zip([1, 2, 3])
        self.assertEqual(c.dict(), dict(zip(['a', 'b', 'c'], [1, 2, 3])))
