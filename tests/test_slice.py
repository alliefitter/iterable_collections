import unittest

from iterable_collections import collect


class TestSlice(unittest.TestCase):

    def test_middle_list(self):
        c = collect([1, 2, 3, 4, 5, 6, 7, 8]).slice(4, 6)
        self.assertEqual(c.list(), [1, 2, 3, 4, 5, 6, 7, 8][4:6])

    def test_beginning_list(self):
        c = collect([1, 2, 3, 4, 5, 6, 7, 8]).slice(0, 4)
        self.assertEqual(c.list(), [1, 2, 3, 4, 5, 6, 7, 8][:4])

    def test_end_list(self):
        c = collect([1, 2, 3, 4, 5, 6, 7, 8]).slice(4)
        self.assertEqual(c.list(), [1, 2, 3, 4, 5, 6, 7, 8][4:])

    def test_negative_list(self):
        c = collect([1, 2, 3, 4, 5, 6, 7, 8]).slice(-1)
        self.assertEqual(c.list(), [1, 2, 3, 4, 5, 6, 7, 8][-1:])

    def test_middle_set(self):
        c = collect({1, 2, 3, 4, 5, 6, 7, 8}).slice(4, 6)
        self.assertEqual(c.set(), set(list({1, 2, 3, 4, 5, 6, 7, 8})[4:6]))

    def test_beginning_set(self):
        c = collect({1, 2, 3, 4, 5, 6, 7, 8}).slice(0, 4)
        self.assertEqual(c.set(), set(list({1, 2, 3, 4, 5, 6, 7, 8})[:4]))

    def test_end_set(self):
        c = collect({1, 2, 3, 4, 5, 6, 7, 8}).slice(4)
        self.assertEqual(c.set(), set(list({1, 2, 3, 4, 5, 6, 7, 8})[4:]))

    def test_negative_set(self):
        c = collect({1, 2, 3, 4, 5, 6, 7, 8}).slice(-1)
        self.assertEqual(c.set(), set(list({1, 2, 3, 4, 5, 6, 7, 8})[-1:]))
    
    def test_middle_tuple(self):
        c = collect((1, 2, 3, 4, 5, 6, 7, 8)).slice(4, 6)
        self.assertEqual(c.tuple(), tuple(list((1, 2, 3, 4, 5, 6, 7, 8))[4:6]))

    def test_beginning_tuple(self):
        c = collect((1, 2, 3, 4, 5, 6, 7, 8)).slice(0, 4)
        self.assertEqual(c.tuple(), tuple(list((1, 2, 3, 4, 5, 6, 7, 8))[:4]))

    def test_end_tuple(self):
        c = collect((1, 2, 3, 4, 5, 6, 7, 8)).slice(4)
        self.assertEqual(c.tuple(), tuple(list((1, 2, 3, 4, 5, 6, 7, 8))[4:]))

    def test_negative_tuple(self):
        c = collect((1, 2, 3, 4, 5, 6, 7, 8)).slice(-1)
        self.assertEqual(c.tuple(), tuple(list((1, 2, 3, 4, 5, 6, 7, 8))[-1:]))
        
    def test_middle_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).slice(1, 3)
        with self.assertRaises(ValueError):
            c.dict()

    def test_beginning_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).slice(0, 2)
        with self.assertRaises(ValueError):
            c.dict()

    def test_end_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).slice(2)
        with self.assertRaises(ValueError):
            c.dict()

    def test_negative_dict(self):
        c = collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).slice(-1)
        with self.assertRaises(ValueError):
            c.dict()
