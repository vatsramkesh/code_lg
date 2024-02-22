"""
Given an 1D integer array A of size N you have to find and return the B largest elements of the array A.
"""

from typing import List
from queue import PriorityQueue


# Time complexity O(N * log(K)), Auxiliary Space: O(K)
def get_k_largest_elements(numbers: List[int], k: int) -> List[int]:
        
        pq = PriorityQueue()
        for i, v in enumerate(numbers):
            pq.put(v)
            if i >= k:
                pq.get()

        # for i in numbers[:k]:
        #     pq.put(i)
            
        # for i in numbers[k:]:
        #     pq.put(i)
        #     pq.get()
            
            
        elements = []
        
        while not pq.empty():
            elements.append(pq.get())
        
        return elements

# This is O(n log n) as we are using sorting
def get_k_largest_elements_using_sorting(numbers: List[int], k: int) -> List[int]:

    numbers.sort()
    return numbers[-k:]



if __name__ == "__main__":
    assert get_k_largest_elements([20, 10, 60, 30, 3, 40, 9, 11, 50], 3) == [40, 50, 60]
    assert get_k_largest_elements([600, 500], 1) == [600]
    assert get_k_largest_elements([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3) == [50, 88, 96 ]
    
    assert get_k_largest_elements_using_sorting([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3) == [50, 88, 96 ]
    assert get_k_largest_elements_using_sorting([600, 500], 1) == [600]
    assert get_k_largest_elements_using_sorting([20, 10, 60, 30, 3, 40, 9, 11, 50], 3) == [40, 50, 60]