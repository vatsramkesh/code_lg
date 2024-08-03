"""
Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:

    d = {}

    for i in range(len(nums)):
        if nums[i] in  d:
            return [d[nums[i]], i]
        # Storing index on target -current val
        d[target-nums[i]] = i
    
    # O(n*n) brute force solution
    for i in range(len(nums)):
        for k, v in enumerate(nums[i+1:], i+1):
            if nums[i] + v == target:
                return [i, k]

if __name__ == "__main__":
    assert two_sum([2 ,7,11,15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]
