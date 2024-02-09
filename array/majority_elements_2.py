"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times
"""

from collections import defaultdict
from typing import List


def majority_elements(nums: List[int]) -> List[int]:
    size = len(nums)

    freq = defaultdict(int)

    for i in nums:
        freq[i]+=1

        if len(freq) <=2:
            continue

        new_freq = defaultdict(int)
        for k, v in freq.items():
            if v > 1:
                new_freq[k] = v-1
        freq = new_freq

    res = []

    for i in freq:
        if freq[i] > size//3:
            res.append(i)
    return res

if __name__ == "__main__":

    assert majority_elements([3, 2, 3]) == [3]
    assert majority_elements([3]) == [3]
    assert majority_elements([3, 2]) == [3, 2]