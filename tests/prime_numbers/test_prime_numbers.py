from algorithms.prime_numbers import pn_basics
from algorithms.prime_numbers import min_perimeter
import unittest


class TestPrimeNumbersBasics(unittest.TestCase):
    def testPrimeDivisors(self):
        self.assertEqual(2, pn_basics.count_divisors(3))
        self.assertEqual(2, pn_basics.count_divisors(5))
        self.assertEqual(2, pn_basics.count_divisors(7))
        self.assertEqual(2, pn_basics.count_divisors(9))
        self.assertEqual(2, pn_basics.count_divisors(11))
        self.assertEqual(2, pn_basics.count_divisors(13))

    def test1(self):
        self.assertEqual(6, pn_basics.count_divisors(20))

    def testMinPerimeter(self):
        self.assertEqual(22, min_perimeter.solution(30))
        self.assertEqual(4, min_perimeter.solution(1))
