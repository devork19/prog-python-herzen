import unittest
from laba2 import idk


class TestIdkFunction(unittest.TestCase):

    def test_basic_case(self):
        result = idk([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_middle_elements(self):
        result = idk([3, 2, 4], 6)
        self.assertEqual(result, [1, 2])

    def test_duplicate_elements(self):
        result = idk([3, 3], 6)
        self.assertEqual(result, [0, 1])

    def test_no_solution(self):
        result = idk([1, 2, 3], 10)
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        result = idk([-1, -2, -3, 5], 2)
        self.assertEqual(result, [2, 3])

    def test_zero_and_positive(self):
        result = idk([0, 4, 3, 0], 0)
        self.assertEqual(result, [0, 3])


if __name__ == '__main__':
    unittest.main()