"""
Given a matrix of 0 and 1s find the submatrix with max area(matrix will be rectangle shape)
"""

from largest_rectangle_in_histogram import largest_rectangle_area_using_stack

def largest_area_of_submatrix(heights) -> int:
    current_row = heights[0]
    # Use the prev logic of histogram here for each row. First find for first row
    # then since for each item height would be 1 or 0 so if its 1 add to prev row and if 0 make it 0 while building
    # the new row on line 17, 19, then call histogram fun for new row again but new heights of bar
    ans = largest_rectangle_area_using_stack(current_row)

    for row in heights[1:]:
        for i, col in enumerate(row):
            if col == 1:
                current_row[i]+=1
            else:
                current_row[i] = 0
        ans = max(ans, largest_rectangle_area_using_stack(current_row))


    return ans

if __name__ == "__main__":
    matrix = [           # Current row(incrementing where 1 or making 0), area
        [1, 1, 0, 1, 1], # [1, 1, 0, 1, 1]  2
        [1, 1, 1, 1, 1], # [2, 2, 1, 2, 2]  5
        [0, 1, 1, 1, 1], # [0, 3, 2, 3, 3]  8
        [1, 1, 1, 1, 1], # [1, 4, 3, 4, 4]  12
        [1, 0, 1, 1, 1], # [2, 0, 4, 5, 5]  12
        [1, 1, 1, 1, 1], # [3, 1, 5, 6, 6]  15 here(last 3 bar can have 5+5+5)
    ]
    assert largest_area_of_submatrix(matrix) == 15