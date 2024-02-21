"""
Find the kth smallest element in an unsorted array.
"""
from typing import List
from queue import PriorityQueue

# Here we create a maxHeap of size K then compare peak of max heap(which should be max of heap) with next item in array
# and if peak > current element the pop the peak and insert current item it will run heapify automatically, 
# continue this till end of array, at the end we will have max heap of size k, since its max 
# heap so peak will be max of heap of size k and it contain kth elemet so peak will be kth smallest.
def kth_smallest_element(numbers: List[int], k: int) -> int:

    pq = PriorityQueue()

    for num in numbers[:k]:
        pq.put(num)

    for num in numbers[k:]:
        if pq.queue[0] > num:
            pq.get()
            pq.put(num)
    e = pq.get()
    print(e)
    return e



if __name__ == "__main__":
    assert kth_smallest_element([20, 10, 60, 30, 3, 40, 9, 11, 50], 3) == 10