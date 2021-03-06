import unittest

from iterable_collections import collect


class TestConcatDict(unittest.TestCase):

    def test_list_and_list(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(list(range(10, 20)))

    def test_list_and_set(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(set(range(10, 20)))

    def test_list_and_tuple(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(tuple(range(10, 20)))

    def test_list_and_iter(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(iter(range(10, 20)))

    def test_list_and_dict(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3})

    def test_list_and_dict_keys(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.keys())

    def test_list_and_dict_items(self):
        c = collect(list(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.items())

    def test_set_and_list(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(list(range(10, 20)))

    def test_set_and_set(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(set(range(10, 20)))

    def test_set_and_tuple(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(tuple(range(10, 20)))

    def test_set_and_iter(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(iter(range(10, 20)))

    def test_set_and_dict(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3})

    def test_set_and_dict_keys(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.keys())

    def test_set_and_dict_items(self):
        c = collect(set(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.items())

    def test_tuple_and_list(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(list(range(10, 20)))

    def test_tuple_and_set(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(set(range(10, 20)))

    def test_tuple_and_tuple(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(tuple(range(10, 20)))

    def test_tuple_and_iter(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(iter(range(10, 20)))

    def test_tuple_and_dict(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3})

    def test_tuple_and_dict_keys(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.keys())

    def test_tuple_and_dict_items(self):
        c = collect(tuple(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.items())

    def test_iter_and_list(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(list(range(10, 20)))

    def test_iter_and_set(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(set(range(10, 20)))

    def test_iter_and_tuple(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(tuple(range(10, 20)))

    def test_iter_and_iter(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict(iter(range(10, 20)))

    def test_iter_and_dict(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3})

    def test_iter_and_dict_keys(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.keys())

    def test_iter_and_dict_items(self):
        c = collect(iter(range(10)))
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.items())

    def test_dict_and_list(self):
        c = collect({'a': 1, 'b': 2, 'c': 3})
        with self.assertRaises(ValueError):
            c.concat_dict(list(range(10, 20)))

    def test_dict_and_set(self):
        c = collect({'a': 1, 'b': 2, 'c': 3})
        with self.assertRaises(ValueError):
            c.concat_dict(set(range(10, 20)))

    def test_dict_and_tuple(self):
        c = collect({'a': 1, 'b': 2, 'c': 3})
        with self.assertRaises(ValueError):
            c.concat_dict(tuple(range(10, 20)))

    def test_dict_and_iter(self):
        c = collect({'a': 1, 'b': 2, 'c': 3})
        with self.assertRaises(ValueError):
            c.concat_dict(iter(range(10, 20)))

    def test_dict_and_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_dict({'a': 2, 'd': 4, 'e': 5})
        d = {'a': 1, 'b': 2, 'c': 3}
        d.update({'a': 2, 'd': 4, 'e': 5})
        self.assertEqual(c.iterable, d)

    def test_dict_and_dict_keys(self):
        c = collect({'a': 1, 'b': 2, 'c': 3})
        with self.assertRaises(ValueError):
            c.concat_dict({'a': 1, 'b': 2, 'c': 3}.keys())

    def test_dict_and_dict_items(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_dict({'a': 2, 'd': 4, 'e': 5}.items())
        d = {'a': 1, 'b': 2, 'c': 3}
        d.update(dict({'a': 2, 'd': 4, 'e': 5}.items()))
        self.assertEqual(c.iterable, d)
