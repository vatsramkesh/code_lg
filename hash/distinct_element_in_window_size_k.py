"""
Count the distinct element in every window of size k
"""

from collections import Counter
from typing import List

def distinct_elements_count(elements: List[int], k: int) :
    
    distinct_counts = []
    for i in range(k, len(elements)+1):
        distinct_counts.append(len(set(elements[i-k:i])))

    return distinct_counts

def distinct_elements_count_optimised(elements: List[int], k: int) :
    
    distinct_counts = []
    # Using start and end two pointers
    start = 0
    end = k
    s = Counter(elements[:k])
    distinct_counts.append(len(s))
    # This is optimised as we aren't recreating set everytime , space O(k), time O(n)
    while end < len(elements):

        if s.get(elements[start]) > 1:
            s[elements[start]]-=1
        else:
            s.pop(elements[start])
        
        # Can use defaultdict to optimized it
        if s.get(elements[end]):
            s[elements[end]] +=1
        else:
            s[elements[end]] = 1

        distinct_counts.append(len(s))

        end+=1
        start+=1

    return distinct_counts

if __name__ == "__main__":
    assert distinct_elements_count([1, 2, 2, 1, 3, 1, 1, 3], 4) == [2, 3, 3, 2, 2]
    assert distinct_elements_count_optimised([1, 2, 2, 1, 3, 1, 1, 3], 4) == [2, 3, 3, 2, 2]
        