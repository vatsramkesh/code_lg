
from typing import List

def search_infinite(numbers: List[int], elem: int) -> int:

    found = False
    end = 1
    start = 0

    # Exponential increment step end here, time complexity O(logn)
    try:
        while elem > numbers[end]:
            start = end
            end = end * 2
    except IndexError:
        return binary_search(numbers, elem, start, end)

    return binary_search(numbers, elem, start, end)

def binary_search(numbers: List[int], elem: int, start: int, end: int) -> int:
    

    while start < end:
        mid = (start + end)//2
        if numbers[mid] == elem:
            return mid

        if numbers[mid] > elem:
            end = mid-1
        else:
            start = mid+1
    return -1
    




if __name__ == "__main__":
    assert search_infinite([1, 3, 7, 8, 12, 34, 58, 67, 89, 98], 58) == 6 
    assert search_infinite([1, 3, 7, 8, 12, 34, 58, 67, 89, 98, 112, 138, 167], 112) == 10
    # assert search_infinite([1, 3, 7, 8, 12, 34, 58, 67, 89, 98], 91) == -1
    # assert binary_search([1, 3, 7, 8, 12, 34, 58, 67, 89, 98], 58, 0, 10) == 6 