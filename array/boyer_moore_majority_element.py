"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.
 """


from collections import defaultdict
from typing import List

def majorityElement(nums: List[int]) -> int:
    size = len(nums)
    num = 0
    count = 0

    # Using Boyer moore algo Time O(n), space O(1)
    for v in nums:
        if count == 0:
            num = v

        count+= (1 if v == num else -1)
    count = 0
    for i in nums:
        if i == num:
            count+=1
        if count > size/2:
            return num
    return -1
    
    # Using hash map Time O(n), space O(n)
    freq = defaultdict(int)

    for i in nums:
        freq[i]+=1

    for k, v in freq.items():
        if v > size/2:
            return k
    return -1


if __name__ == "__main__":
    assert majorityElement([1, 2, 3, 1, 2, 1, 1]) == 1
    assert majorityElement([1, 2]) == -1