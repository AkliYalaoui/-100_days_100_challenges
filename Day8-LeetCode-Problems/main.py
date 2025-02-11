import unittest
from products import product_except_self

class TestLeetCodeAlgorithms(unittest.TestCase):
    def test_product_except_self(self):
        nums = [1,2,3,4]
        answer = product_except_self(nums)
        self.assertEqual(answer, [24,12,8,6])

        nums = [-1,1,0,-3,3]
        answer = product_except_self(nums)
        self.assertEqual(answer, [0,0,9,0,0])

if __name__ == "__main__" :
    unittest.main()