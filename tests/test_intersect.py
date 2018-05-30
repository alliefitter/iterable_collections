import unittest

from iterable_collections import collect


class TestIntersect(unittest.TestCase):

    def test_list_and_list(self):
        c = collect(list(range(10))).intersect(list(range(0, 5)))
        self.assertEqual(c.iterable, set(range(10)) & set(list(range(0, 5))))

    def test_list_and_set(self):
        c = collect(list(range(10))).intersect(set(range(0, 5)))
        self.assertEqual(c.iterable, set(range(10)) & set(set(range(0, 5))))

    def test_list_and_tuple(self):
        c = collect(list(range(10))).intersect(tuple(range(0, 5)))
        self.assertEqual(c.iterable, set(range(10)) & set(tuple(range(0, 5))))

    def test_list_and_iter(self):
        c = collect(list(range(10))).intersect(iter(range(0, 5)))
        self.assertEqual(c.iterable, set(list(range(10))) & set(iter(range(0, 5))))

    def test_list_and_dict(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.intersect({'a': 1, 'b': 2, 'c': 3})

    def test_list_and_dict_keys(self):
        c = collect(list(range(10))).intersect({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, set(range(10)) & set({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_list_and_dict_items(self):
        c = collect(list(range(10))).intersect({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, set(range(10)) & set({'a': 1, 'b': 2, 'c': 3}.items()))

    def test_set_and_list(self):
        c = collect(set(range(10))).intersect(list(range(0, 5)))
        self.assertEqual(c.iterable, set(set(range(10))) & set(list(range(0, 5))))

    def test_set_and_set(self):
        c = collect(set(range(10))).intersect(set(range(0, 5)))
        self.assertEqual(c.iterable, set(set(range(10))) & set(set(range(0, 5))))

    def test_set_and_tuple(self):
        c = collect(set(range(10))).intersect(tuple(range(0, 5)))
        self.assertEqual(c.iterable, set(set(range(10))) & set(tuple(range(0, 5))))

    def test_set_and_iter(self):
        c = collect(set(range(10))).intersect(iter(range(0, 5)))
        self.assertEqual(c.iterable, set(set(range(10))) & set(iter(range(0, 5))))

    def test_set_and_dict(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.intersect({'a': 1, 'b': 2, 'c': 3})

    def test_set_and_dict_keys(self):
        c = collect(set(range(10))).intersect({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, set(set(range(10))) & set({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_set_and_dict_items(self):
        c = collect(set(range(10))).intersect({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, set(set(range(10))) & set({'a': 1, 'b': 2, 'c': 3}.items()))

    def test_tuple_and_list(self):
        c = collect(tuple(range(10))).intersect(list(range(0, 5)))
        self.assertEqual(c.iterable, set(tuple(range(10))) & set(list(range(0, 5))))

    def test_tuple_and_set(self):
        c = collect(tuple(range(10))).intersect(set(range(0, 5)))
        self.assertEqual(c.iterable, set(tuple(range(10))) & set(set(range(0, 5))))

    def test_tuple_and_tuple(self):
        c = collect(tuple(range(10))).intersect(tuple(range(0, 5)))
        self.assertEqual(c.iterable, set(tuple(range(10))) & set(tuple(range(0, 5))))

    def test_tuple_and_iter(self):
        c = collect(tuple(range(10))).intersect(iter(range(0, 5)))
        self.assertEqual(c.iterable, set(tuple(range(10))) & set(iter(range(0, 5))))

    def test_tuple_and_dict(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.intersect({'a': 1, 'b': 2, 'c': 3})

    def test_tuple_and_dict_keys(self):
        c = collect(tuple(range(10))).intersect({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, set(tuple(range(10))) & set({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_tuple_and_dict_items(self):
        c = collect(tuple(range(10))).intersect({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, set(tuple(range(10))) & set({'a': 1, 'b': 2, 'c': 3}.items()))

    def test_iter_and_list(self):
        c = collect(iter(range(10))).intersect(list(range(0, 5)))
        self.assertEqual(c.iterable, set(iter(range(10))) & set(list(range(0, 5))))

    def test_iter_and_set(self):
        c = collect(iter(range(10))).intersect(set(range(0, 5)))
        self.assertEqual(c.iterable, set(iter(range(10))) & set(set(range(0, 5))))

    def test_iter_and_tuple(self):
        c = collect(iter(range(10))).intersect(tuple(range(0, 5)))
        self.assertEqual(c.iterable, set(iter(range(10))) & set(tuple(range(0, 5))))

    def test_iter_and_iter(self):
        c = collect(iter(range(10))).intersect(iter(range(0, 5)))
        self.assertEqual(c.iterable, set(iter(range(10))) & set(iter(range(0, 5))))

    def test_iter_and_dict(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.intersect({'a': 1, 'b': 2, 'c': 3})

    def test_iter_and_dict_keys(self):
        c = collect(iter(range(10))).intersect({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, set(iter(range(10))) & set({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_iter_and_dict_items(self):
        c = collect(iter(range(10))).intersect({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, set(iter(range(10))) & set({'a': 1, 'b': 2, 'c': 3}.items()))

    def test_dict_and_list(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).intersect(list(range(0, 5)))
        self.assertEqual(c.iterable, set({'a': 1, 'b': 2, 'c': 3}) & set(list(range(0, 5))))

    def test_dict_and_set(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).intersect(set(range(0, 5)))
        self.assertEqual(c.iterable, set({'a': 1, 'b': 2, 'c': 3}) & set(set(range(0, 5))))

    def test_dict_and_tuple(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).intersect(tuple(range(0, 5)))
        self.assertEqual(c.iterable, set({'a': 1, 'b': 2, 'c': 3}) & set(tuple(range(0, 5))))

    def test_dict_and_iter(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).intersect(iter(range(0, 5)))
        self.assertEqual(c.iterable, set({'a': 1, 'b': 2, 'c': 3}) & set(iter(range(0, 5))))

    def test_dict_and_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).intersect({'a': 2, 'd': 4, 'e': 5})
        self.assertEqual(
            c.iterable,
            set(dict({'a': 1, 'b': 2, 'c': 3}).items()) & set(dict({'a': 2, 'd': 4, 'e': 5}).items())
        )

    def test_dict_and_dict_keys(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).intersect({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, set({'a': 1, 'b': 2, 'c': 3}) & set({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_dict_and_dict_items(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).intersect({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, set({'a': 1, 'b': 2, 'c': 3}) & set({'a': 1, 'b': 2, 'c': 3}.items()))
