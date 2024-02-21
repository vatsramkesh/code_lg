from typing import List

from heapify import build_heap, heapify



def heap_sort(numbers: List[int]):
    build_heap(numbers)
    for i in range(len(numbers)-1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers, 0, i)

if __name__ == "__main__":
    heap = [40, 10, 30, 50, 60, 15]
    heap_sort(heap)
    assert heap == [10, 15, 30, 40, 50, 60]