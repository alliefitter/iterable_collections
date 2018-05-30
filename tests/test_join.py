from unittest import TestCase

from iterable_collections import collect


class TestJoin(TestCase):
    def test_list_of_str(self):
        self.assertEqual('a,b,c,d', collect(['a', 'b', 'c', 'd']).join(','))
        
    