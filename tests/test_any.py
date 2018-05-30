import unittest

from iterable_collections import collect


class TestAny(unittest.TestCase):

    def test_true_all(self):
        c = collect([True, True, True])
        self.assertTrue(c.any())

    def test_true_mixed(self):
        c = collect([True, False, True])
        self.assertTrue(c.any())

    def test_false(self):
        c = collect([False, False, False])
        self.assertFalse(c.any())

    def test_falsey_true(self):
        c = collect([True, {}, []])
        self.assertTrue(c.any())

    def test_falsey_false(self):
        c = collect([None, {}, []])
        self.assertFalse(c.any())
