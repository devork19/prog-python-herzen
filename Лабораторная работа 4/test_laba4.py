import unittest
from laba4 import gen_bin_tree


class MyTestCase(unittest.TestCase):
    def test_zero_height(self):
        result = gen_bin_tree(height=0)
        self.assertIsNone(result)

    def test_one_height(self):
        result = gen_bin_tree(height=1, root=5)
        self.assertEqual(result['root'], 5)
        self.assertIsNone(result['left'])
        self.assertIsNone(result['right'])

    def test_default_root(self):
        result = gen_bin_tree()
        self.assertEqual(result['root'], 9)

    def test_left_calc(self):
        result = gen_bin_tree(height=2, root=9)
        self.assertEqual(result['left']['root'], 19)

    def test_right_calc(self):
        result = gen_bin_tree(height=2, root=9)
        self.assertEqual(result['right']['root'], 17)

    def test_different_root(self):
        result = gen_bin_tree(height=2, root=3)
        self.assertEqual(result['root'], 3)

    def test_leaves_none(self):
        result = gen_bin_tree(height=2, root=9)
        self.assertIsNone(result['left']['left'])

    def test_custom_formula(self):
        result = gen_bin_tree(height=2, root=10,
                              left_branch=lambda x: x + 1)
        self.assertEqual(result['left']['root'], 11)


if __name__ == '__main__':
    unittest.main()
