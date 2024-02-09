import math


def max_sum_subarray(nums: list[int]) -> int:

    max_sum = 0
    current_sum = 0
    start = 0
    end = len(nums)-1

    # Kadane's algo O(n) time complexity
    for i, v in enumerate(nums):
        if current_sum <= 0:
            start = i

        current_sum = current_sum+v
        if max_sum < current_sum:
            max_sum = current_sum
            end = i
        # max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum, nums[start:end+1]



    # Brute force O(n2)
    max_sum = nums[0]
    for i, v in enumerate(nums):
        s = v
        for j in nums[i+1:]:
            s = s+j
            max_sum = max(max_sum, s)
    return max_sum


if __name__ == "__main__":
    assert max_sum_subarray([-5, 4, 6, -3, 4, -1]) == (11, [4, 6, -3, 4])
    assert max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]) == (6, [4, -1, 2, 1])
    assert max_sum_subarray([5,4,-1,7,8]) == (23, [5,4,-1,7,8])
    assert max_sum_subarray([1]) == (1, [1])
    