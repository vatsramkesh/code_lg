
from typing import List



def binary_search(numbers: List[int], elem: int) -> int:
    
    start = 0
    end = len(numbers)-1
    while start <= end:
        mid = (start + end)//2

        if numbers[mid] == elem:
            return mid

        # left part is sorted
        if numbers[mid] > numbers[start]:
            if elem >= numbers[start] and elem < numbers[mid]:
                end = mid-1
            else:
                start = mid+1
        # right part is sorted
        else:
            if elem >= numbers[mid] and elem <= numbers[end]:
                start = mid+1
            else:
                end = mid-1

    return -1
    




if __name__ == "__main__":
    assert binary_search([20, 30, 40, 50, 60, 5, 10], 5) == 5 
    assert binary_search([20, 30, 40, 50, 60, 5, 10], 10) == 6
    assert binary_search([20, 30, 40, 50, 60, 5, 10], 20) == 0
    assert binary_search([20, 30, 40, 50, 60, 5, 10], 111) == -1 