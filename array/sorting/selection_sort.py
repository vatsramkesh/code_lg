

from typing import List

def selection_sort(numbers: List[int]) -> List[int]:

    l = len(numbers)
    # Time O(n2), space O(1)
    for i in range(l-1):
        min_idx = i
        for j in range(i+1, l):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        if min_idx != i:
            numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]
        

    return numbers

if __name__ == "__main__":
    assert selection_sort([4, 3, 7, 1, 5]) == [1, 3, 4, 5, 7]
    assert selection_sort([8, 4, 1, 5, 9, 2]) == [1, 2, 4, 5, 8, 9]
