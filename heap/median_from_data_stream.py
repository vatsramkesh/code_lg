"""
Approach: Create two heaps, all the number less than median should be in left(maxHeap) and greater than
median should be in right(min heap). Number of element in heap should be nearly equal with atmost 1 diff.
So median could be max of left heap(peak since its maxHeap, O(1)) or min of right heap(peak since its min heap), 
or sum of peak of both/2.

Approach2: addNum just append the num to python list and then when we call findMedian then first sort the nums list 
and find the median:
`
def findMedian(self):
    self.nums.sort()
    l = len(self.nums)
    if l%2:
        return self.nums[l//2]
    else:
        return sum(self.nums[l//2-1:l//2+1])/2
`
here sorting everytime take O(n log n)
"""
import heapq

class MedianFinder():

    def __init__(self):
        # initialize two heaps small and large, small is maxHeap and large will be min heap
        # heaps should be of approx equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # First add every number to small/max heap, Since small is max heap and Python default heap in min heap so
        #  multiplying number by -1 so extracting from it will give you max of heap
        heapq.heappush(self.small, -1 * num)

        # Make sure every element in smalll should be less than every element in large heap
        # We can just compare the peak as these are min/max heaps
        if (self.small and self.large and -1 * self.small[0] > self.large[0]):
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        # Uneven size
        if len(self.small) > len(self.large) +1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        if len(self.large) > len(self.small) + 1: 
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

    def findMedian(self) -> float:
        # print(self.small)
        # print(self.large)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1* self.small[0] + self.large[0])/2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(8)
    mf.addNum(7)
    assert mf.findMedian() == 4.5
    mf.addNum(17)
    assert mf.findMedian() == 7