"""
You are given two integer arrays of equal length target and arr. In one step, 
you can select any non-empty subarray of arr and reverse it. 
You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

"""

from collections import Counter, defaultdict
from typing import List


def can_be_equal(target: List[int], arr: List[int]) -> bool:
    # Use counter to count freq of each and compare if equal
    # return Counter(target) == Counter(arr)

    freq = defaultdict(int)
    for i, v in zip(target, arr):
        # Here increment freq by one for each item in target and decrement for each in arr
        # and at last run loop it must be 0 freq for each element
        freq[i]+=1
        freq[v]-=1
    for i in target:
        if freq[i] != 0:
            return False
    return True

    tc = defaultdict(int)
    ac = defaultdict(int)

    # Since both are of equal len, keep count of each item in both arr
    for i in range(len(target)):
        tc[target[i]] += 1
        ac[arr[i]] += 1
    return tc == ac



if __name__ == "__main__":
    assert can_be_equal([1,2,3,4], [2,4,1,3]) == True
    assert can_be_equal(target = [3,7,9], arr = [3,7,11]) == False
    assert can_be_equal([7], [7]) == True