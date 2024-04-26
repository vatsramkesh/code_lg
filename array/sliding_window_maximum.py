"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very 
left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.
"""

import collections
from typing import List
from queue import PriorityQueue


def max_sliding_window_using_list_only( nums: List[int], k: int) -> List[int]:
    output = []
    # Time complexity is O(n*k)
    # O(k) to find max out of k

    for i in range(len(nums)+1-k):
        output.append(max(nums[i:i+k]))

    return output

def max_sliding_window( nums: List[int], k: int) -> List[int]:

    output = []

    # Using dequeue, time complexity O(n) using dequeue
    d = collections.deque()
    for i, n in enumerate(nums):
        # print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, output))
        while d and nums[d[-1]] < n:
            d.pop()
            # print("\t Popped from d because d has elements and nums[d.top] < curr element")
        d.append(i)

        if d[0] == i - k:
            d.popleft()
            # print("\t Popped left from d because it's outside the window's leftmost (i-k)")
        if i>=k-1:
            output.append(nums[d[0]])
            # print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
    return output

def min_sliding_window( nums: List[int], k: int) -> List[int]:
    # Using PriorityQueue as well
    output = []
    q = PriorityQueue()
    for i in range(k):
        q.put(nums[i])
    
    for i in range(k, len(nums)-1):
        # if q.queue[0]
        output.append(q.get())
        q.put(nums[i])

    output = []
    # Time complexity is O(n*k)
    # O(k) to find max out of k
    for i in range(len(nums)+1-k):
        output.append(max(nums[i:i+k]))
    return output


if __name__ == "__main__":
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([4, 1, 3, 5, 1, 2, 3, 2, 1, 2, 5], 3) == [4, 5, 5, 5, 3, 3, 3, 2, 5]

    assert max_sliding_window_using_list_only([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert max_sliding_window_using_list_only([1], 1) == [1]
    assert max_sliding_window_using_list_only([4, 1, 3, 5, 1, 2, 3, 2, 1, 2, 5], 3) == [4, 5, 5, 5, 3, 3, 3, 2, 5]