from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product
    of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    """

    output = [1] * len(nums)
    left = 1
    for i in range(len(nums)):
        output[i] *= left
        left *= nums[i]
    
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]

    return output        