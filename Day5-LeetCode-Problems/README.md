# Day5-LeetCode-Problems

This directory contains solutions to two common algorithm challenges:

1. **Merge Sorted Array**
2. **Remove Element**

The solutions are implemented in Python and tested using the `unittest` framework.

---

## Challenges

### 1. Merge Sorted Array

Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array. The number of elements initialized in `nums1` and `nums2` are `m` and `n` respectively. You may assume that `nums1` has enough space (size ≥ `m + n`) to hold additional elements from `nums2`.

**Example:**
```python
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Result: [1,2,2,3,5,6]
```

### 2. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Return the number of elements in nums which are not equal to val.

**Example:**
```python
nums = [3,2,2,3], val = 3

Result: k = 2, nums = [2,2,_,_]
```