import unittest
from jump_game import can_jump, can_jump_2
from h_index import hIndex
from randomized_set import RandomizedSet

class TestLeetCodeAlgorithms(unittest.TestCase):
    def test_can_jump(self):
        nums = [2,3,1,1,4]
        jumpable = can_jump(nums)
        # Jump 1 step from index 0 to 1, then 3 steps to the last index.
        self.assertEqual(jumpable, True)

        nums = [3,2,1,0,4]
        jumpable = can_jump(nums)
        # You will always arrive at index 3 no matter what.
        # Its maximum jump length is 0, which makes it impossible to reach the last index.
        self.assertEqual(jumpable, False)

    def test_can_jump_2(self):
        nums = [2,3,1,1,4]
        jump_length = can_jump_2(nums)
        # The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
        # then 3 steps to the last index.
        self.assertEqual(jump_length, 2)

        nums = [2,3,0,1,4]
        jump_length = can_jump_2(nums)
        self.assertEqual(jump_length, 2)
    
    def test_hindex(self):
        citations = [3,0,6,1,5]
        h = hIndex(citations)
        self.assertEqual(h, 3)

        citations = [1,3,1]
        h = hIndex(citations)
        self.assertEqual(h, 1)

    def test_randomized(self):
        randomizedSet =  RandomizedSet()
        self.assertEqual(randomizedSet.insert(1), True)
        self.assertEqual(randomizedSet.remove(2), False)
        self.assertEqual(randomizedSet.insert(2), True)
        self.assertIn(randomizedSet.getRandom(), [1, 2])
        self.assertEqual(randomizedSet.remove(1), True)
        self.assertEqual(randomizedSet.insert(2), False)
        self.assertEqual(randomizedSet.getRandom(), 2)


if __name__ == "__main__":
    unittest.main()