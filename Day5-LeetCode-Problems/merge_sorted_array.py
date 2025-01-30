from typing import List

def merge(nums1: List[int], n: int, nums2: List[int], m:int) -> None :
    """
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
    be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
    """
    j = 0
    for i in range(n + m) :
        if j >=m :
            break
        if  nums1[i] > nums2[j] : 
            for k in range(n+j, i, -1):
                nums1[k] = nums1[k-1]
            nums1[i] = nums2[j]
            j += 1

        if  i >= n + j :
            nums1[i] = nums2[j]
            j += 1

            