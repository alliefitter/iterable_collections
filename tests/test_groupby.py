import unittest
from collections import namedtuple
from itertools import groupby
from random import randint

from iterable_collections import collect


class TestGroupby(unittest.TestCase):

    def test_lists(self):
        test = [[randint(0, 10) for _ in range(9)] for _ in range(10)]
        c = collect(test).sorted(key=lambda x: x[3]) \
            .groupby(key=lambda x: x[3]) \
            .map(lambda x: (x[0], list(x[1])))
        self.assertEqual(
            c.list(),
            list(map(lambda x: (x[0], list(x[1])), groupby(sorted(test, key=lambda x: x[3]), key=lambda x: x[3])))
        )

    def test_dicts(self):
        test = list(map(lambda x: dict(zip('abcdefghi', x)), [[randint(0, 10) for _ in range(9)] for _ in range(10)]))
        c = collect(test).sorted(key=lambda x: x['c']) \
            .groupby(key=lambda x: x['c']) \
            .map(lambda x: (x[0], list(x[1])))
        self.assertEqual(
            c.list(),
            list(map(lambda x: (x[0], list(x[1])), groupby(sorted(test, key=lambda x: x['c']), key=lambda x: x['c'])))
        )

    def test_tuples(self):
        test = list(map(lambda x: (list(zip('abcdefghi', x))), [[randint(0, 10) for _ in range(9)] for _ in range(10)]))
        c = collect(test).sorted(key=lambda x: x[3][1]) \
            .groupby(key=lambda x: x[3][1]) \
            .map(lambda x: (x[0], list(x[1])))
        self.assertEqual(
            c.list(),
            list(map(lambda x: (x[0], list(x[1])), groupby(sorted(test, key=lambda x: x[3][1]), key=lambda x: x[3][1])))
        )

    def test_namedtuples(self):
        test = list(map(namedtuple('TestData', 'a b c d e f g h i')._make,
                        [[randint(0, 10) for _ in range(9)] for _ in range(10)]))
        c = collect(test).sorted(key=lambda x: x.c) \
            .groupby(key=lambda x: x.c) \
            .map(lambda x: (x[0], list(x[1])))
        self.assertEqual(
            c.list(),
            list(map(lambda x: (x[0], list(x[1])), groupby(sorted(test, key=lambda x: x.c), key=lambda x: x.c)))
        )
