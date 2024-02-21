"""
Given an array of integers, find the length of the longest sub-sequence 
such that elements in the subsequence are consecutive integers, 
the consecutive numbers can be in any order. 
"""
from typing import List

def dfs(num, longest):

    if num not in longest:
        return 0
    
    if longest[num] != 0:
        return longest[num]

    current_max = 1 + dfs(num+1, longest)
    longest[num] = current_max
    return current_max

def longest_consecutive(nums):
    if len(nums) <= 1:
        return len(nums)

    max_length = 1
    longest = {}

    for num in nums:
        longest[num] = 0

    for num in nums:
        max_length = max(max_length, dfs(num, longest))
    
    return max_length

def longest_consecutive_using_sorting(nums: List[int]) -> int:

    nums.sort()
    longest = 1
    consecutive_len = 1

    for n in range(1, len(nums[1:])):
        # print("ttttttt: ", nums[n], "   ssssss: ", nums[n-1], longest)
        if nums[n] - nums[n-1] == 1:
            longest+=1
        elif nums[n] == nums[n-1]:
            continue
        else:
            longest = 1
        consecutive_len = max(consecutive_len, longest)
    # print(longest)
    return consecutive_len


if __name__ == "__main__":
    # For this time complexity in linear O(n) and space is also O(n) used by dict
    assert longest_consecutive([1, 9, 3, 10, 4, 20, 2]) == 4
    assert longest_consecutive([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]) == 5

    # This solution takes O(n log n) as we use sort func and then iterate over array and space is constant O(1)
    assert longest_consecutive_using_sorting([1, 9, 3, 10, 4, 20, 2]) == 4
    assert longest_consecutive_using_sorting([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]) == 5

    