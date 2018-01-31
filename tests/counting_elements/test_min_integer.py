import unittest
from algorithms.counting_elements import min_integer


class TestMinInteger(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(5, min_integer.solution([1, 3, 6, 4, 1, 2]))
