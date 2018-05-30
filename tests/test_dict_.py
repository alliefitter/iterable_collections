import unittest

from iterable_collections import collect


class TestDict_(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.dict_()

    def test_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.dict_()

    def test_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.dict_()

    def test_iterator(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.dict_()

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.dict_().iterable, dict({'a': 1, 'b': 2}))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(c.dict_().iterable, dict({'a': 1, 'b': 2}.items()))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate()
        self.assertEqual(c.dict_().iterable, dict(enumerate(range(10))))

    def test_list_of_tuples(self):
        c = collect([('a', 1), ('b', 2), ('c', 3)])
        self.assertEqual(c.dict_().iterable, dict([('a', 1), ('b', 2), ('c', 3)]))

    def test_map_of_tuples_from_list_of_dicts(self):
        c = collect([{'a': 'foo', 'b': 1}, {'a': 'bar', 'b': 2}, {'a': 'baz', 'b': 3}])\
            .map(lambda x: (x['a'], x['b']))
        self.assertEqual(c.dict_().iterable, {'foo': 1, 'bar': 2, 'baz': 3})

    def test_zip(self):
        c = collect(['a', 'b', 'c']).zip([1, 2, 3])
        self.assertEqual(c.dict_().iterable, {'a': 1, 'b': 2, 'c': 3})
