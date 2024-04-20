"""
Given an array of integers, find the nearest smaller number for every element
such that the smaller element is on the left side.
"""

from typing import List

def smaller_elements(numbers: List) -> List[int]:
    # O(n**2)
    new_array = [-1]

    for i, v in enumerate(numbers[1:], 1):
        if v >= numbers[i-1]:
            new_array.append(numbers[i-1])
        else:
            for k in new_array[::-1]:
                if k <= v:
                    new_array.append(k)
                    break

    return new_array


def smaller_elements_using_stack(numbers: List) -> List[int]:
    my_stack = []
    output = []

    for v in numbers:
        # compare top of the stack
        while my_stack and my_stack[-1] >= v:
            my_stack.pop()

        # For empty stack add -1
        if not my_stack:
            output.append(-1)
            print(-1, end=", ")
        else:
            output.append(my_stack[-1])
            print(my_stack[-1], end=", ")

        my_stack.append(v)

    print()
    return output


if __name__ == "__main__":

    assert smaller_elements([4, 10, 5, 8, 20, 15, 3, 12]) == [-1, 4, 4, 5, 8, 8, -1, 3]
    # print(smaller_elements([5, 15, 20, 25, 5, 12, 20]))
    assert smaller_elements([5, 15, 20, 25, 12, 20]) == [-1, 5, 15, 20, 5, 12]

    assert smaller_elements_using_stack([4, 10, 5, 8, 20, 15, 3, 12]) == [-1, 4, 4, 5, 8, 8, -1, 3]
    # print(smaller_elements([5, 15, 20, 25, 5, 12, 20]))
    assert smaller_elements_using_stack([5, 15, 20, 25, 12, 20]) == [-1, 5, 15, 20, 5, 12]