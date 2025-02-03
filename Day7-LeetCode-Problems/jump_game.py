from typing import List

def can_jump(nums: List[int]) -> bool:
    """
    You are given an integer array nums. You are initially positioned at the array's first index, 
    and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    """
    
    n = len(nums)
    if n <= 1 : 
        return True 

    if 0 not in nums : 
        return True

    stack = [0]
    visited = set() 

    while len(stack) > 0 : 
        current = stack.pop()
        if current in visited:
            continue  
        visited.add(current)

        for i in range(nums[current], 0, - 1):
            next_index = current + i
            if next_index >= n - 1 : 
                return True
            if next_index not in visited:
                stack.append(next_index)

    return False
        

def can_jump_2(nums: List[int]) -> int:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, 
    if you are at nums[i], you can jump to any nums[i + j] where:
        0 <= j <= nums[i] and
        i + j < n
    Return the minimum number of jumps to reach nums[n - 1]. 
    The test cases are generated such that you can reach nums[n - 1].
    """
    n = len(nums)
    if n <= 1:
        return 0 
    current_range = 0
    j = 0
    reach = 0

    for i in range(n - 1) : 
        reach = max(reach, i + nums[i])
        if i == current_range:
            j += 1
            current_range = reach
            
    return j

