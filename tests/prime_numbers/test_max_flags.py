from algorithms.prime_numbers import max_flags_nlogn
import unittest


class TestMaxFlagsBinary(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, max_flags_nlogn.solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
        self.assertEqual(1, max_flags_nlogn.solution([1, 5, 3]))

    def test_bisect(self):
        max

