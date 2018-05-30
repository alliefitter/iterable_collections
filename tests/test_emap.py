import unittest

from iterable_collections import collect
from iterable_collections.utils import spread_tuple_parameter


class TestEMap(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).emap(lambda i, x: i + x * 2)
        self.assertEqual(
            c.list(),
            list(map(*spread_tuple_parameter(lambda i, x: i + x * 2), enumerate(list(range(10)))))
        )

    def test_set(self):
        c = collect(set(range(10))).emap(lambda i, x: i + x * 2)
        self.assertEqual(
            c.list(),
            list(map(*spread_tuple_parameter(lambda i, x: i + x * 2), enumerate(list(range(10)))))
        )

    def test_tuple(self):
        c = collect(tuple(range(10))).emap(lambda i, x: i + x * 2)
        self.assertEqual(
            c.list(),
            list(map(*spread_tuple_parameter(lambda i, x: i + x * 2), enumerate(list(range(10)))))
        )

    def test_iterator(self):
        c = collect(iter(range(10))).emap(lambda i, x: i + x * 2)
        self.assertEqual(
            c.list(),
            list(map(*spread_tuple_parameter(lambda i, x: i + x * 2), enumerate(list(range(10)))))
        )

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).emap(lambda i, x: str(i) + x * 2)
        self.assertEqual(
            c.list(),
            list(map(*spread_tuple_parameter(lambda i, x: str(i) + x * 2), enumerate(list({'a': 1, 'b': 2}))))
        )

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).emap(lambda i, x: (i,) + x)
        self.assertEqual(
            c.list(),
            list(map(*spread_tuple_parameter(lambda i, x: (i,) + x), enumerate(list({'a': 1, 'b': 2}.items()))))
        )

