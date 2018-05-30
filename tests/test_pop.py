import unittest

from iterable_collections import collect


class TestPop(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10)))
        self.assertEqual(c.pop(), list.pop(list(list(range(10)))))
        self.assertEqual(c.len(), 9)
        c.pop()
        self.assertEqual(c.len(), 8)

    def test_set(self):
        c = collect(set(range(10)))
        self.assertEqual(c.pop(), list.pop(list(set(range(10)))))
        self.assertEqual(c.len(), 9)
        c.pop()
        self.assertEqual(c.len(), 8)

    def test_tuple(self):
        c = collect(tuple(range(10)))
        self.assertEqual(c.pop(), list.pop(list(tuple(range(10)))))
        self.assertEqual(c.len(), 9)
        c.pop()
        self.assertEqual(c.len(), 8)

    def test_iterator(self):
        c = collect(iter(range(10)))
        self.assertEqual(c.pop(), list.pop(list(iter(range(10)))))
        self.assertEqual(c.len(), 9)
        c.pop()
        self.assertEqual(c.len(), 8)

    def test_dict(self):
        c = collect({'a': 1, 'b': 2})
        self.assertEqual(c.pop(), list.pop(list({'a': 1, 'b': 2})))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items())
        self.assertEqual(c.pop(), list.pop(list({'a': 1, 'b': 2}.items())))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate()
        self.assertEqual(c.pop(), list.pop(list(enumerate(range(10)))))
        self.assertEqual(c.len(), 9)
        c.pop()
        self.assertEqual(c.len(), 8)

