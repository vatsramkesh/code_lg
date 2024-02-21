"""
Find the kth largest element in an unsorted array.
"""
from typing import List
from queue import PriorityQueue

# Here we create a minHeap(Python PriorityQueue create min heap for us) of size K
# then compare peak of min heap(which should be minimum of heap) with next item in array
# and if peak < current element the pop the peak and insert current item it will run heapify automatically, 
# continue this till end of array, at the end we will have min heap of size k, since its min 
# heap so peak will be minimum of heap and it contain k elemet so peak will be kth largest.
def kth_largest_element(numbers: List[int], k: int) -> int:

    pq = PriorityQueue()

    for num in numbers[:k]:
        pq.put(num)

    for num in numbers[k:]:
        if pq.queue[0] < num:
            pq.get()
            pq.put(num)

    return pq.get()

# This is O(n log n)
def kth_largest_using_sorting(numbers: List[int], k: int) -> int:
    numbers.sort()
    return numbers[-k]



if __name__ == "__main__":
    assert kth_largest_element([20, 10, 60, 30, 3, 40, 9, 11, 50], 3) == 40
    assert kth_largest_using_sorting([20, 10, 60, 30, 3, 40, 9, 11, 50], 3) == 40