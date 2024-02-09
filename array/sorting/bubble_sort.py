
from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:

    l = len(numbers)
    # Time O(n2), space O(1)
    for i in range(l):
        is_swappable = False
        for j in range(l-1-i):
            if numbers[j]>numbers[j+1]:
                is_swappable = True
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        if not is_swappable:
            # break
            return numbers

    return numbers

if __name__ == "__main__":
    assert bubble_sort([4, 3, 7, 1, 5]) == [1, 3, 4, 5, 7]