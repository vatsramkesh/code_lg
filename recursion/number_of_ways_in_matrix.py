"""
There is a robot on an m x n grid. The robot is initially located
 at the top-left corner (i.e., grid[0][0]). The robot tries to move
 to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
 The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible 
unique paths that the robot can take to reach the bottom-right corner.
"""

# @cache
def unique_paths(n: int, m: int) -> int:
    # if in last row/column the there will be only 1 way to move
    # print("n = ", n, " andddd m = ", m)
    if n == 1 or m == 1:
        return 1
    
    return unique_paths(n, m-1) + unique_paths(n-1, m)


# This is much efficient
def find_unique_path(n: int, m: int) -> int:
    """
    The idea behind this approach is to use a 2D Dynamic Programming (DP) 
    array to store the number of unique paths to each cell. 
    A cell (i,j)(i, j)(i,j) can be reached either from
     (i−1,j)(i-1, j)(i−1,j) or (i,j−1)(i, j-1)(i,j−1), and thus the number 
     of unique paths to (i,j)(i, j)(i,j) is the sum of the number of unique 
     paths to these two cells.
    """
    dp = [[1 if i == 0 or j == 0 else 0 for i in range(n)] for j in range(m)]
    print(dp)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp)
    return dp[-1][-1]


if __name__ == "__main__":
    a = unique_paths(3, 7)
    print(a)
    assert a == 28
    assert unique_paths(2, 3) == 3

    assert find_unique_path(3, 7) == 28
    assert find_unique_path(2, 3) == 3