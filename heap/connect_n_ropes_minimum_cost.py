"""
Given are N ropes of different lengths, the task is to connect these ropes into one rope with minimum cost, 
such that the cost to connect two ropes is equal to the sum of their lengths.
"""


from typing import List
from queue import PriorityQueue

# Time complexity of this solution will be O(n log n) used by put, 
# get and again put so overall will be O(n log n).
# So here we are using the PriorityQueue(use min heap), at each point peak will be the min item,
# and cost of adding two min length ropes is minimum so we pop two peak items add them to ans a
# nd then add them back to queue, do this untill array is empty
# This is efficient solution
def minimum_cost(ropes: List[int]) -> int:

    cost = 0
    pq = PriorityQueue()

    for rope in ropes:
        pq.put(rope)

    while not pq.empty():
        first = pq.get()
        if not pq.empty():
            second = pq.get()
            total = first +second
            cost+=total
            pq.put(total)
        
    return cost

# Time complexity of this solution will be O(n) * O(n log n)
def minimum_cost_usin_sorting(ropes: List[int]) -> int:

    cost = 0
    # pq = PriorityQueue()

    a = len(ropes)
    ropes.sort()

    while a > 1:
        first = ropes.pop(0)
        second = ropes.pop(0)
        cost += first+second
        ropes.append(first+second)
        ropes.sort()
        a-=1
        
    return cost

if __name__ == "__main__":
    assert minimum_cost([4, 3, 2, 6]) == 29
    assert minimum_cost([1, 18]) == 19
    assert minimum_cost([2, 5, 4, 8, 6, 9]) == 85
    assert minimum_cost([4, 3, 2]) == 14

    assert minimum_cost_usin_sorting([4, 3, 2, 6]) == 29
    assert minimum_cost_usin_sorting([2, 5, 4, 8, 6, 9]) == 85
    assert minimum_cost_usin_sorting([4, 3, 2]) == 14
    assert minimum_cost_usin_sorting([1, 18]) == 19