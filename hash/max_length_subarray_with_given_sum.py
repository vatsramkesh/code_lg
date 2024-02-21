"""
Find the subarray with given sum
We keep mapping of sum and index till current index and then check 
if we have current_sum-desired_sum in map this mean current index is end index
and value where current_sum-desired_sum will be starting index

if current_sum-desired_sum in map that mean we found our array and
index for current_sum-desired_sum is our startinf index
"""

from typing import List
from collections import defaultdict

def max_length_subarray_sum(numbers: List, sum_number: int):
    sum_mapping = defaultdict(list)
    current_sum = 0
    start = 0
    end = -1
    max_length = 0
    # Time complexity O(n) also space complexity O(n) due to map
    for i, v in enumerate(numbers):
        current_sum +=v
        
        if current_sum-sum_number == 0:
            start = 0
            end = i
            max_length = max(end-start, max_length)

        if sum_mapping.get(current_sum-sum_number):
            start = min(sum_mapping[current_sum-sum_number]) + 1
            end = i+1
            max_length = max(end-start, max_length)
        
        sum_mapping[current_sum].append(i)

    if end == -1:
        return "Not Found"
        
    return max_length

def subarray_maxlen_brute_force(numbers: List, sum_number: int):

    # Time complexity is O(n2)
    max_len = 0
    for i in range(len(numbers)):
        s = numbers[i]
        for j in range(i+1, len(numbers)):
            s+= numbers[j]
            if s == sum_number:
                max_len = max(max_len, j+1-i)
            
    return max_len


def largest_subarray_with_equal_zeros_and_one(numbers: List):
    # Trick is to replace all 0 with -1 and then check for max subarray sum 0
    for idx, num in enumerate(numbers):
        if num == 0:
            numbers[idx] = -1
        
    return max_length_subarray_sum(numbers, 0)


if __name__ == "__main__":
    assert subarray_maxlen_brute_force([10, 15, -5, 15, -10, 5], 5) ==  4
    assert max_length_subarray_sum([10, 15, -5, 15, -10, 5], 5) == 4
    assert largest_subarray_with_equal_zeros_and_one([1, 1, 0, 1, 1, 0, 0]) == 6




