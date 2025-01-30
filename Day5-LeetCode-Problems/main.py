import unittest
from merge_sorted_array import merge
from remove_element import remove_element

class TestAlgorithms(unittest.TestCase) :

    def test_merge_sorted_arrays(self) :
        nums1 = [1,2,3,0, 0 ,0]
        nums2 = [4,5,6]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,3,4,5,6])

        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3

        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,2,3,5,6])

        nums1 = [4,0,0,0,0,0]
        m = 1
        nums2 = [1,2,3,5,6]
        n = 5

        merge(nums1, m, nums2,n)
        self.assertEqual(nums1, [1,2,3,4,5,6])

    def test_remove_element(self):
        nums = [3,2,2,3]
        n = 4
        val = 3

        k = remove_element(nums, val)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [2,2])

        nums = [0,1,2,2,3,0,4,2]
        n = 8
        val = 2

        k = remove_element(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0,1,3,0,4])


if __name__ == "__main__":
    unittest.main()