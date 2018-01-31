import unittest
from algorithms.counting_elements import perm_check


class TestPermCheck(unittest.TestCase):
    def test_double(self):
        self.assertEqual(0, perm_check.solution([1, 1]))

    def test_simple_true(self):
        self.assertEqual(1, perm_check.solution([4, 1, 3, 2]))

    def test_simple_false(self):
        self.assertEqual(0, perm_check.solution([4, 1, 3, 2, 1]))

    def test_simple_false_2(self):
        self.assertEqual(0, perm_check.solution([9, 5, 7, 3, 2, 7, 3, 1, 10, 8]))


if __name__ == '__main__':
    unittest.main()
