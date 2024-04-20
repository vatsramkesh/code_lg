"""
Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

from typing import List
# Import isn't working here somehow, so coping func in this file as well
# from stack.smaller_element_index import get_previous_smaller_element_index, get_next_smaller_element_index

def largest_rectangle_area(heights: List[int]) -> int:

    largest_area = heights[0]
    # Here time complexity will be O(n**2) as we running nested loop
    for i, v in enumerate(heights):
        # Idea is for each element calculate the left and right index(
            # every element on left and right sould be bigger than current to avoid overflow) till where it can go
        left = i
        right = i
        while left >=0 and v <= heights[left]:
            left-=1
        while right <len(heights) and v <= heights[right] :
            right+=1
        # print(i, v, largest_area)
        
        largest_area = max(largest_area, (right-left-1)*heights[i])
    return largest_area

def largest_rectangle_area_using_stack(heights: List[int]) -> int:

    largest_area = heights[0]
    prev_smaller = get_previous_smaller_element_index(heights)
    next_smaller = get_next_smaller_element_index(heights)
    
    # Here time complexity will be O(n) as we doing 3 iterations(1 for prev_smaller, 1 for next_smaller and 1 here)
    for i, v in enumerate(heights):
        
        largest_area = max(largest_area, (next_smaller[i]-prev_smaller[i]-1)*heights[i])
    return largest_area

def get_previous_smaller_element_index(heights: List[int]) -> List[int]:
    
    output = []
    my_stack = []

    for i, height in enumerate(heights):

        while my_stack and heights[my_stack[-1]] >= height:
            my_stack.pop()

        if not my_stack:
            output.append(-1)
        else:
            output.append(my_stack[-1])
        my_stack.append(i)


    return output


def get_next_smaller_element_index(heights: List[int]) -> List[int]:
    
    output = []
    my_stack = []
    
    k = len(heights) - 1
    # Start from right to left here, for rightmost element or when stack is empty mean
    #  there is no smaller element on right or next side of current element push len of array index in output, 
    # otherwise keep fetching top of stack while we get smaller element element index
    for i in range(k, -1, -1):

        while my_stack and heights[my_stack[-1]] >= heights[i]:
            my_stack.pop()

        # For empty stack add -1
        if not my_stack:
            output.append(k+1)
        else:

            output.append(my_stack[-1])

        my_stack.append(i)


    return output[::-1]


def largestRectangleArea(heights: List[int]) -> int:
        ans = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>=h:
                index,hei = stack.pop()
                start = index
                ans = max(ans,(i-index)*hei)
            stack.append((start,h))

        for i,h in stack:
            ans = max(ans,(len(heights)-i)*h)

        return ans

if __name__ == "__main__":

    assert largest_rectangle_area([2,1,5,6,2,3]) == 10
    assert largest_rectangle_area([2, 4]) == 4

    assert largest_rectangle_area_using_stack([2,1,5,6,2,3]) == 10
    assert largest_rectangle_area_using_stack([2, 4]) == 4