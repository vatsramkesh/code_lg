"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after raining.
"""
from typing import List


def trap(height: List[int]) -> int:
    # using two pointers time O(n), space O(1)

    left, right = 0, len(height)-1
    left_max = height[left]
    right_max = height[right]
    water_qty = 0
    while left <right:
        if left_max < right_max:
            left+=1
            left_max = max(left_max, height[left])
            water_qty += left_max-height[left]
        else:
            right-=1
            right_max = max(right_max, height[right])
            water_qty += right_max-height[right]
        
    return water_qty

    l = len(height)
    left = [height[0]]
    right = [0]*l
    right[-1] = height[-1]
    # formula min(max(left), max(right))-height[i], time and space O(n)
    for i in range(1, l):
        left.append(max(left[i-1], height[i]))
    
    for i in range(l-2, -1, -1):
        right[i] = max(right[i+1], height[i])
    
    water_qty = 0
    for i in range(l-1):
        water_qty+=min(left[i], right[i])-height[i]
    return water_qty



if __name__ == "__main__":

    assert trap([4,2,0,3,2,5]) == 9
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6