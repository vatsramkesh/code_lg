"""
Given an array of integers, find the nearest smaller number for every element
such that the smaller element is on the right side.
"""

from typing import List

# def smaller_elements(numbers: List) -> List[int]:
#     # O(n**2)
#     new_array = [-1]

#     for i, v in enumerate(numbers[1:], 1):
#         if v >= numbers[i-1]:
#             new_array.append(numbers[i-1])
#         else:
#             for k in new_array[::-1]:
#                 if k <= v:
#                     new_array.append(k)
#                     break

#     return new_array


def smaller_elements_right_using_stack(numbers: List) -> List[int]:
    my_stack = []
    output = []

    for v in range(len(numbers)-1, -1, -1):

        while my_stack and my_stack[-1] > numbers[v]:
            my_stack.pop()

        # For empty stack add -1
        if not my_stack:
            output.append(-1)
        else:

            output.append(my_stack[-1])

        my_stack.append(numbers[v])


    return output[::-1]


if __name__ == "__main__":
   
    assert smaller_elements_right_using_stack([3, 10, 5, 1, 15, 10, 7, 6]) == [1, 5, 1, -1, 10, 7, 6, -1]