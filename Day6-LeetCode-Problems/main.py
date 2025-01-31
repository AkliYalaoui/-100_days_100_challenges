import unittest
from remove_duplicates_sorted_array \
import remove_duplicates_sorted_array, remove_duplicates_sorted_array_2
from majority_element import  majority_element
from rotate_array import rotate
from max_profit import max_profit, max_profit2

class TestLeetCodeAlgorithms(unittest.TestCase):

    def test_remove_duplicates_from_sorted_array(self):
        nums = [1,1,2]
        k = remove_duplicates_sorted_array(nums)

        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1,2])

        nums = [0,0,1,1,1,2,2,3,3,4]
        k = remove_duplicates_sorted_array(nums)

        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0,1,2,3,4])

    
    def test_remove_duplicates_from_sorted_array_2(self):
        nums = [1,1,1,2,2,3]
        k = remove_duplicates_sorted_array_2(nums)

        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1,1,2,2,3])

        nums = [0,0,1,1,1,1,2,3,3]
        k = remove_duplicates_sorted_array_2(nums)

        self.assertEqual(k, 7)
        self.assertEqual(nums[:k], [0,0,1,1,2,3,3])

    def test_majority_element(self):
        nums = [3,2,3]
        n = majority_element(nums)
        self.assertEqual(n , 3)

        nums = [2,2,1,1,1,2,2]
        n = majority_element(nums)
        self.assertEqual(n , 2)

    def test_rotate(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        rotate(nums, k)
        self.assertEqual(nums, [5,6,7,1,2,3,4])

        nums = [-1,-100,3,99]
        k = 2
        rotate(nums, k)
        self.assertEqual(nums, [3,99,-1,-100])

    def test_max_profit(self):

        prices = [7,1,5,3,6,4]
        M = max_profit(prices)
        self.assertEqual(M, 5)

        prices = [7,6,4,3,1]
        M = max_profit(prices)
        self.assertEqual(M, 0)

    def test_max_profit2(self):

        prices = [7,1,5,3,6,4]
        M = max_profit2(prices)
        self.assertEqual(M, 7)

        prices = [1,2,3,4,5]
        M = max_profit2(prices)
        self.assertEqual(M, 4)

        prices = [7,6,4,3,1]
        M = max_profit2(prices)
        self.assertEqual(M, 0)


if __name__ == "__main__":
    unittest.main()