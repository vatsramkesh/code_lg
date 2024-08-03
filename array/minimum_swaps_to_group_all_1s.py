"""
Given an array of 0’s and 1’s, we need to write a program to find the 
minimum number of swaps required to group all 1’s present in the array together.
"""
from typing import List


def min_swap(nums: List[int]) -> int:

    total_ones = nums.count(1)

    min_swaps = total_ones 

    # Take window and count number of 0 in each window of number of 1s.
    # Here O(n) for outer loop then to calculate number of zero in each window size lets say O(k)
    # So this is not efficient solution doesn't works for min_swap([0, 1, 1]) == 0
    
    # for i in range(len(nums)-total_ones):
    #     min_swaps = min(min_swaps, nums[i:i+total_ones].count(0))
        
    # return min_swaps

    current_zeros = 0
    # calculating 0 in first window
    for i in range(total_ones):
        if nums[i] == 0:
            current_zeros += 1
    
    min_swaps = current_zeros

    # Here only one loop and then inc/dec variable do time complexity will be O(n) only.
    for i in range(total_ones, len(nums)):
        # Number we are removing from window, if its zero decrement count by 1
        if nums[i-total_ones] == 0:
            current_zeros -= 1
        # new Number adding to window if its zero increment count by 1
        if nums[i] == 0:
            current_zeros += 1
        min_swaps = min(min_swaps, current_zeros)
    
    return min_swaps


if __name__ == "__main__":
    assert min_swap([1, 0, 1]) == 1
    assert min_swap([0, 1, 1]) == 0
    assert min_swap([0, 1, 0, 0, 0]) == 0
    assert min_swap([1, 0, 1, 0, 1]) == 1
    assert min_swap([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]) == 3
