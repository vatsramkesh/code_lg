

from typing import List

def quick_sort(numbers: List[int], first: int, last: int) -> List[int]:

    if first < last:
        pivot_idx = partition(numbers, first, last)
        quick_sort(numbers, 0, pivot_idx-1)
        quick_sort(numbers, pivot_idx+1, last)


def partition(a, l, h):
    pivot = l
    while (l < h):
        while(l < h and a[l] <= a[pivot]):
            l+=1

        while (a[h] > a[pivot]):
            h-=1
        if l < h:
            a[l], a[h] = a[h], a[l]
    if pivot != h:
        a[pivot], a[h] = a[h], a[pivot]
    return h

if __name__ == "__main__":
    number_array = [4, 3, 7, 1, 5]
    quick_sort(number_array, 0, 4) 
    assert number_array == [1, 3, 4, 5, 7]
    
    number_array = [8, 4, 1, 5, 9, 2]
    quick_sort(number_array, 0, 5) 
    assert number_array == [1, 2, 4, 5, 8, 9]
