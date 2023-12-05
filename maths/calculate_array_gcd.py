""" Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""

def get_gcd(numbers: list[int]) -> int:

    def gcd_of_two_numbers(a, b) -> int:
        if b == 0:
            return a
        # gcd_of_two_numbers(60, 24) -> gcd_of_two_numbers(24, 12) -> gcd_of_two_numbers(12, 0)
        return gcd_of_two_numbers(b, a%b)
    numbers.sort()
    return gcd_of_two_numbers(numbers[-1], numbers[0])

def find_gcd(numbers: int) -> int:

    a = max(numbers)
    b = min(numbers)

    for i in range(b, 0, -1):
        if not a%i and not b%i:
            return i




if __name__ == "__main__":
    assert get_gcd([24, 36, 60]) == 12

    assert get_gcd([2,5,6,9,10]) == 2

    assert get_gcd([7,5,6,8,3]) == 1

    assert get_gcd([3, 3]) == 3


    assert find_gcd([24, 36, 60]) == 12

    assert find_gcd([2,5,6,9,10]) == 2

    assert find_gcd([7,5,6,8,3]) == 1

    assert find_gcd([3, 3]) == 3

    # assert get_gcd(1) == 0

    # assert get_primes(-1991) == False
