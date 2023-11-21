# Find the two non-repeting element in an array where all other elements repeats exactly twice
# https://leetcode.com/problems/single-number-iii/

def get_non_repeating(numbers: list[int]) -> tuple:

    res = 0

    for i in numbers:
        res = res^abs(i)

    # res is XOR of two non repeting number then we need to find out these two nuber out of it

    # Find the right most set bit of res
    rmsb = res & -res

    # time O(n), space O(1)
    x, y = 0, 0
    for i in numbers:
        i = abs(i)
        if (rmsb & i) == 0:
            # Numbers where bit in off
            x = x ^ i
        else:
            # Numbers where bit is set
            y = y ^ i

    return x, y

    # OR time and space both O(n)
    # return [i for i, j in Counter(nums).items() if j == 1] 

    
if __name__ == "__main__":

    elements = get_non_repeating([5, 4, 1, 3, 4, 1, 5, 9])
    assert  3 in elements 
    assert 9 in elements

    elements = get_non_repeating([0, 4, 1, 3, -4, 1, 10, 0])
    assert  3 in elements 
    assert 10 in elements