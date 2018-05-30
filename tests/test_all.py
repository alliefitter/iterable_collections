import unittest

from iterable_collections import collect


class TestAll(unittest.TestCase):

    def test_true(self):
        c = collect([True, True, True])
        self.assertTrue(c.all())

    def test_false(self):
        c = collect([True, False, True])
        self.assertFalse(c.all())

    def test_falsey(self):
        c = collect([None, {}, []])
        self.assertFalse(c.all())
