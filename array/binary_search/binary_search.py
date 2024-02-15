
from typing import List

def binary_search_iterative(nums: List[int], elem: int) -> int:

    l, r = 0, len(nums) - 1

    while (l<=r):
        mid = (l+r)//2
        
        if nums[mid] == elem:
            return mid
        
        if nums[mid] > elem:
            r = mid-1
        else:
            l = mid+1
    return -1

def binary_search_recursive(nums: List[int], elem: int, l: int, r: int) -> int:
    if l > r:
        return -1

    mid = (l+r)//2
    if nums[mid] == elem:
        return mid
        
    elif nums[mid] > elem:
        return binary_search_recursive(nums, elem, l, mid-1)
    else:
        return binary_search_recursive(nums, elem, mid+1, r)


if __name__ == "__main__":
    assert binary_search_iterative([-4, -1, 3, 7, 17], 7) == 3
    assert binary_search_iterative([-4, -1, 3, 7, 17], 11) == -1
    
    assert binary_search_recursive([-4, -1, 3, 7, 17], 7, 0, 5) == 3
    assert binary_search_recursive([-4, -1, 3, 7, 17], 11, 0, 5) == -1
