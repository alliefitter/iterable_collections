import unittest
from collections import namedtuple
from random import randint

from iterable_collections import collect


class TestSorted(unittest.TestCase):

    def test_list(self):
        test = [randint(0, 10) for _ in range(9)]
        c = collect(test).sorted()
        self.assertEqual(c.iterable, sorted(test))

    def test_set(self):
        test = {randint(0, 10) for _ in range(9)}
        c = collect(test).sorted()
        self.assertEqual(c.iterable, sorted(test))

    def test_tuple(self):
        test = tuple(randint(0, 10) for _ in range(9))
        c = collect(test).sorted()
        self.assertEqual(c.iterable, sorted(test))

    def test_iterator(self):
        test = [randint(0, 10) for _ in range(9)]
        c = collect(iter(test)).sorted()
        self.assertEqual(c.iterable, sorted(iter(test)))

    def test_dict(self):
        test = dict(zip('abcdefghi', [randint(0, 10) for _ in range(9)]))
        c = collect(test).sorted()
        self.assertEqual(c.iterable, sorted(test))

    def test_dict_items(self):
        test = dict(zip('abcdefghi', [randint(0, 10) for _ in range(9)]))
        c = collect(test.items()).sorted()
        self.assertEqual(c.iterable, sorted(test.items()))

    def test_enumerate(self):
        test = [randint(0, 10) for _ in range(9)]
        c = collect(test).enumerate().sorted()
        self.assertEqual(list(c.iterable), list(enumerate(test)))

    def test_lists(self):
        test = [[randint(0, 10) for _ in range(9)] for _ in range(10)]
        c = collect(test).sorted(key=lambda x: x[3])
        self.assertEqual(
            c.iterable,
            list(sorted(test, key=lambda x: x[3]))
        )

    def test_dicts(self):
        test = list(map(lambda x: dict(zip('abcdefghi', x)), [[randint(0, 10) for _ in range(9)] for _ in range(10)]))
        c = collect(test).sorted(key=lambda x: x['c'])
        self.assertEqual(
            c.iterable,
            list(sorted(test, key=lambda x: x['c']))
        )

    def test_tuples(self):
        test = list(map(lambda x: (list(zip('abcdefghi', x))), [[randint(0, 10) for _ in range(9)] for _ in range(10)]))
        c = collect(test).sorted(key=lambda x: x[3][1])
        self.assertEqual(
            c.iterable,
            list(sorted(test, key=lambda x: x[3][1]))
        )

    def test_namedtuples(self):
        test = list(map(namedtuple('TestData', 'a b c d e f g h i')._make,
                        [[randint(0, 10) for _ in range(9)] for _ in range(10)]))
        c = collect(test).sorted(key=lambda x: x.c)
        self.assertEqual(
            c.iterable,
            list(sorted(test, key=lambda x: x.c))
        )
