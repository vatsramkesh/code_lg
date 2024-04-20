
from typing import List

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


if __name__ == "__main__":
    assert get_previous_smaller_element_index([4, 2, 1, 5, 6, 3, 2, 4, 2]) == [-1, -1, -1, 2, 3, 2, 2, 6, 2]

    assert get_next_smaller_element_index([4, 2, 1, 5, 6, 3, 2, 4, 2]) == [1, 2, 9, 5, 5, 6, 9, 8, 9]