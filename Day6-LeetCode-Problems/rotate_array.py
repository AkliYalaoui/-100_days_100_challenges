from typing import List

def rotate(nums: List[int],k :int) -> None : 
    """
        Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    """

    n = len(nums)
    k = k % n
    unrotated = nums.copy()
    for i in range(n) : 
        nums[(i + k) % n] = unrotated[i]

    