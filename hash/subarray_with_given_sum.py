"""
Find the subarray with given sum
"""

from typing import List

def subarray_sum(numbers: List, sum_number: int):
    sum_mapping = {}
    s = 0
    start = 0
    end = -1
    subarray_index = set()
    for i, v in enumerate(numbers):
        s +=v
        print(s)
        if s-sum_number == 0:
            start = 0
            end = i
            break

        if sum_mapping.get(s-sum_number):
            start = sum_mapping[s-sum_number] + 1
            end = i
            # subarray_index.add((start, end+1))
            break
        
        sum_mapping[s] = i
    if end == -1:
        return end
    return (start, end)

def subarray_brute_force(numbers: List, sum_number: int):

    subarrays = set()
    # Time complexity is O(n2)
    for i in range(len(numbers)):
        s = numbers[i]
        for j in range(i+1, len(numbers)):
            s+= numbers[j]
            if s == sum_number:
                subarrays.add((i,j))
            

    return subarrays


if __name__ == "__main__":
    # (-5, 15, -10, 5), (15, -10)
    # assert subarray_brute_force([10, 15, -5, 15, -10, 5], 5) == {(2, 5), (3, 4)}
    print(subarray_sum([10, 15, -5, 15, -10, 5], 5))




