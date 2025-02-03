# Day7-LeetCode-Problems
This repository contains tests for different algorithms based on common LeetCode problems. The tests are written using Python's `unittest` framework.
The following algorithms are tested in the project:

1. **Jump Game (can_jump)**
2. **Jump Game II (can_jump_2)**
3. **H-Index**
4. **Randomized Set**

## Test Cases

1. **Test: `can_jump`**
   - **Description**: The `can_jump` function checks if you can reach the last index of an array, starting from the first index, where each element represents the maximum number of indices you can jump forward.
   - **Test Case 1**: 
     - Input: `[2, 3, 1, 1, 4]`
     - Expected Output: `True`
     - Explanation: You can jump 1 step from index 0 to 1, and then jump 3 steps to the last index, making it possible to reach the last index.
   - **Test Case 2**: 
     - Input: `[3, 2, 1, 0, 4]`
     - Expected Output: `False`
     - Explanation: You will always reach index 3 no matter what. Its maximum jump length is 0, making it impossible to reach the last index.

2. **Test: `can_jump_2`**
   - **Description**: The `can_jump_2` function calculates the minimum number of jumps needed to reach the last index of an array.
   - **Test Case 1**:
     - Input: `[2, 3, 1, 1, 4]`
     - Expected Output: `2`
     - Explanation: The minimum number of jumps is 2. Jump 1 step from index 0 to 1, then jump 3 steps to the last index.
   - **Test Case 2**:
     - Input: `[2, 3, 0, 1, 4]`
     - Expected Output: `2`
     - Explanation: The minimum number of jumps is 2. Jump 2 steps from index 0 to 1, then 3 steps to the last index.

3. **Test: `hIndex`**
   - **Description**: The `hIndex` function calculates the h-index from a list of citation counts. The h-index is the highest number `h` such that the researcher has `h` papers with at least `h` citations.
   - **Test Case 1**:
     - Input: `[3, 0, 6, 1, 5]`
     - Expected Output: `3`
     - Explanation: The h-index is 3, because there are 3 papers with at least 3 citations.
   - **Test Case 2**:
     - Input: `[1, 3, 1]`
     - Expected Output: `1`
     - Explanation: The h-index is 1, because there is only one paper with at least 1 citation.

4. **Test: `RandomizedSet`**
   - **Description**: The `RandomizedSet` class supports insertion, deletion, and random retrieval of elements, with each operation being done in constant time.
   - **Test Case 1**:
     - Action: Insert `1`
     - Expected Output: `True`
     - Explanation: The insertion of 1 is successful.
   - **Test Case 2**:
     - Action: Remove `2`
     - Expected Output: `False`
     - Explanation: Removing 2 is not possible because 2 has not been inserted yet.
   - **Test Case 3**:
     - Action: Insert `2`
     - Expected Output: `True`
     - Explanation: The insertion of 2 is successful.
   - **Test Case 4**:
     - Action: Get a random element
     - Expected Output: Random value between 1 and 2
     - Explanation: The `getRandom()` function randomly returns an element from the set.
   - **Test Case 5**:
     - Action: Remove `1`
     - Expected Output: `True`
     - Explanation: The removal of 1 is successful.
   - **Test Case 6**:
     - Action: Insert `2` again
     - Expected Output: `False`
     - Explanation: `2` is already in the set.
   - **Test Case 7**:
     - Action: Get a random element
     - Expected Output: `2`
     - Explanation: After the previous operations, `2` is the only remaining element in the set.