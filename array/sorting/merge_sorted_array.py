"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
 To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
 should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    last = m+n-1
    while m >0 and n >0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m-=1
        else:
            nums1[last] = nums2[n-1]
            n-=1
        last-=1

    if n>0:
        nums1[:n] = nums2[:n]
    

            


if __name__ == "__main__":
    nums1 = [1,2,3,9,0,0,0]
    m = 4
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6, 9]
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    assert nums1 == [1]
    