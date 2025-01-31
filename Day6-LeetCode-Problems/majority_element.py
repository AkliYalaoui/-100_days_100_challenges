from typing import List

def majority_element(nums: List[int]) -> int : 
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """

    occurences = {}
    for n in nums : 
        k = occurences.setdefault(n , 0)
        occurences[n] = k + 1
    
    return max(occurences, key= occurences.get)