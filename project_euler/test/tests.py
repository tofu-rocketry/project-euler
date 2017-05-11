# Hack to allow import of ProjectEulerAnswers while it is still at top level.
from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__ )))))

import unittest

import ProjectEulerAnswers as pea


class TestEuler(unittest.TestCase):

    def test_sumofdivs(self):
        self.assertEqual(pea.sum_of_divs(220), 284)

    def test_prob1(self):
        self.assertEqual(pea.prob1(10), 23)

    def test_prob2(self):
        first_ten = (1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
        even_sum = sum(i for i in first_ten if i % 2 == 0)
        self.assertEqual(pea.prob2(90), even_sum)

    def test_prob3(self):
        self.assertEqual(pea.prob3(13195), 29)

    def test_prob4(self):
        self.assertEqual(pea.prob4(2), 9009)

    def test_prob5(self):
        self.assertEqual(pea.prob5(10), 2520)

    def test_prob6(self):
        self.assertEqual(pea.prob6(10), 2640)

    def test_prob7(self):
        self.assertEqual(pea.prob7(6), 13)

    def test_prob10(self):
        # TODO: Check boundary is correct - open/closed
        self.assertEqual(pea.prob10(9), 17)

    def test_prob12(self):
        self.assertEqual(pea.prob12(5), 28)

    def test_prob15(self):
        self.assertEqual(pea.prob15(2), 6)

    def test_prob16(self):
        self.assertEqual(pea.prob16(15), 26)

    def test_prob17(self):
        self.assertEqual(pea.prob17(5), 19)

    def test_prob18(self):
        self.assertEqual(pea.prob18(path.join('..', '..', 'triangle1.txt')), 23)

    def test_prob20(self):
        self.assertEqual(pea.prob20(10), 27)

if __name__ == '__main__':
    unittest.main()
