import unittest
from algorithms.max_slice import max_double_slice


class TestMaxDoubleSlice(unittest.TestCase):
    def test(self):
        self.assertEqual(17, max_double_slice.solution([3, 2, 6, -1, 4, 5, -1, 2]))

    def test2(self):
        self.assertEqual(15, max_double_slice.solution([3, -2, 6, -1, 4, 5, -1, 2]))

    def testIncomplete(self):
        self.assertEqual(17, max_double_slice.solution([5, 17, 0, 3]))

    def test3(self):
        self.assertEqual(1, max_double_slice.solution([5, 0, 1, 0, 5]))

    def test3(self):
        self.assertEqual(10, max_double_slice.solution([0, 10, -5, -2, 0]))

    def test4(self):
        self.assertEqual(0, max_double_slice.solution([-4, -5, -1, -5, -7, -19, -11]))
