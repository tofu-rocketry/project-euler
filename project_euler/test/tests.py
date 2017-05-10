# Hack to allow import of ProjectEulerAnswers while it is still at top level.
from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__ )))))

import unittest

import ProjectEulerAnswers as pea


class TestEuler(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
