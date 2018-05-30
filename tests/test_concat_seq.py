from itertools import chain
import unittest

from iterable_collections import collect


class TestConcatSeq(unittest.TestCase):

    def test_list_and_list(self):
        c = collect(list(range(10))).concat_seq(list(range(10, 20)))
        self.assertEqual(c.iterable, list(range(10)) + list(list(range(10, 20))))

    def test_list_and_set(self):
        c = collect(list(range(10))).concat_seq(set(range(10, 20)))
        self.assertEqual(c.iterable, list(range(10)) + list(set(range(10, 20))))

    def test_list_and_tuple(self):
        c = collect(list(range(10))).concat_seq(tuple(range(10, 20)))
        self.assertEqual(c.iterable, list(range(10)) + list(tuple(range(10, 20))))

    def test_list_and_iter(self):
        c = collect(list(range(10))).concat_seq(iter(range(10, 20)))
        self.assertEqual(list(c.iterable), list(chain(iter(list(range(10))), iter(iter(range(10, 20))))))

    def test_list_and_dict(self):
        c = collect(list(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(list(c.iterable), list(range(10)) + list({'a': 1, 'b': 2, 'c': 3}))

    def test_list_and_dict_keys(self):
        c = collect(list(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, list(range(10)) + list({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_list_and_dict_items(self):
        c = collect(list(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, list(range(10)) + list({'a': 1, 'b': 2, 'c': 3}.items()))

    def test_set_and_list(self):
        c = collect(set(range(10))).concat_seq(list(range(10, 20)))
        self.assertEqual(c.iterable, list(set(range(10))) + list(list(range(10, 20))))

    def test_set_and_set(self):
        c = collect(set(range(10))).concat_seq(set(range(10, 20)))
        self.assertEqual(c.iterable, list(set(range(10))) + list(set(range(10, 20))))

    def test_set_and_tuple(self):
        c = collect(set(range(10))).concat_seq(tuple(range(10, 20)))
        self.assertEqual(c.iterable, list(set(range(10))) + list(tuple(range(10, 20))))

    def test_set_and_iter(self):
        c = collect(set(range(10))).concat_seq(iter(range(10, 20)))
        self.assertEqual(list(c.iterable), list(chain(iter(set(range(10))), iter(iter(range(10, 20))))))

    def test_set_and_dict(self):
        c = collect(set(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(list(c.iterable), list(set(range(10))) + list({'a': 1, 'b': 2, 'c': 3}))

    def test_set_and_dict_keys(self):
        c = collect(set(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, list(set(range(10))) + list({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_set_and_dict_items(self):
        c = collect(set(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, list(set(range(10))) + list({'a': 1, 'b': 2, 'c': 3}.items()))

    def test_tuple_and_list(self):
        c = collect(tuple(range(10))).concat_seq(list(range(10, 20)))
        self.assertEqual(c.iterable, list(tuple(range(10))) + list(list(range(10, 20))))

    def test_tuple_and_set(self):
        c = collect(tuple(range(10))).concat_seq(set(range(10, 20)))
        self.assertEqual(c.iterable, list(tuple(range(10))) + list(set(range(10, 20))))

    def test_tuple_and_tuple(self):
        c = collect(tuple(range(10))).concat_seq(tuple(range(10, 20)))
        self.assertEqual(c.iterable, list(tuple(range(10))) + list(tuple(range(10, 20))))

    def test_tuple_and_iter(self):
        c = collect(tuple(range(10))).concat_seq(iter(range(10, 20)))
        self.assertEqual(list(c.iterable), list(chain(iter(tuple(range(10))), iter(iter(range(10, 20))))))

    def test_tuple_and_dict(self):
        c = collect(tuple(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(list(c.iterable), list(tuple(range(10))) + list({'a': 1, 'b': 2, 'c': 3}))

    def test_tuple_and_dict_keys(self):
        c = collect(tuple(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, list(tuple(range(10))) + list({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_tuple_and_dict_items(self):
        c = collect(tuple(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, list(tuple(range(10))) + list({'a': 1, 'b': 2, 'c': 3}.items()))

    def test_iter_and_list(self):
        c = collect(iter(range(10))).concat_seq(list(range(10, 20)))
        self.assertEqual(c.iterable, list(iter(range(10))) + list(list(range(10, 20))))

    def test_iter_and_set(self):
        c = collect(iter(range(10))).concat_seq(set(range(10, 20)))
        self.assertEqual(c.iterable, list(iter(range(10))) + list(set(range(10, 20))))

    def test_iter_and_tuple(self):
        c = collect(iter(range(10))).concat_seq(tuple(range(10, 20)))
        self.assertEqual(c.iterable, list(iter(range(10))) + list(tuple(range(10, 20))))

    def test_iter_and_iter(self):
        c = collect(iter(range(10))).concat_seq(iter(range(10, 20)))
        self.assertEqual(list(c.iterable), list(chain(iter(iter(range(10))), iter(iter(range(10, 20))))))

    def test_iter_and_dict(self):
        c = collect(iter(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(list(c.iterable), list(iter(range(10))) + list({'a': 1, 'b': 2, 'c': 3}))

    def test_iter_and_dict_keys(self):
        c = collect(iter(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, list(iter(range(10))) + list({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_iter_and_dict_items(self):
        c = collect(iter(range(10))).concat_seq({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, list(iter(range(10))) + list({'a': 1, 'b': 2, 'c': 3}.items()))

    def test_dict_and_list(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_seq(list(range(10, 20)))
        self.assertEqual(c.iterable, list({'a': 1, 'b': 2, 'c': 3}) + list(list(range(10, 20))))

    def test_dict_and_set(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_seq(set(range(10, 20)))
        self.assertEqual(c.iterable, list({'a': 1, 'b': 2, 'c': 3}) + list(set(range(10, 20))))

    def test_dict_and_tuple(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_seq(tuple(range(10, 20)))
        self.assertEqual(c.iterable, list({'a': 1, 'b': 2, 'c': 3}) + list(tuple(range(10, 20))))

    def test_dict_and_iter(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_seq(iter(range(10, 20)))
        self.assertEqual(list(c.iterable), list(chain(iter({'a': 1, 'b': 2, 'c': 3}), iter(iter(range(10, 20))))))

    def test_dict_and_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_seq({'a': 2, 'd': 4, 'e': 5})
        self.assertEqual(c.iterable, list({'a': 1, 'b': 2, 'c': 3}) + list({'a': 2, 'd': 4, 'e': 5}))

    def test_dict_and_dict_keys(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_seq({'a': 1, 'b': 2, 'c': 3}.keys())
        self.assertEqual(c.iterable, list({'a': 1, 'b': 2, 'c': 3}) + list({'a': 1, 'b': 2, 'c': 3}.keys()))

    def test_dict_and_dict_items(self):
        c = collect({'a': 1, 'b': 2, 'c': 3}).concat_seq({'a': 1, 'b': 2, 'c': 3}.items())
        self.assertEqual(c.iterable, list({'a': 1, 'b': 2, 'c': 3}) + list({'a': 1, 'b': 2, 'c': 3}.items()))
