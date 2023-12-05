
"""Given an integer n, return the number of trailing zeroes in n!.
Traditional approach using for loop could be out of memory/time or integer limit 
"""

def number_of_trailing_zeros(number: int) -> int:
    """
    it's essential to understand that trailing zeros result from the 
    multiplication of multiples of 5 and 2. The key is to count the 
    number of 5's and 2's in the multiplication process.
    Number of 5 will always be greater then number of 2 so just count 5
    """
    number_of_zeros = 0

    # time/space complexity O(1)
    while number >= 5:
        number_of_zeros = number_of_zeros + number//5
        number = number//5
    return number_of_zeros

    # OR should also works
    return number/5 + number/25 + number/125 + number/625 + number/3125

if __name__ == "__main__":
    zeros = number_of_trailing_zeros(3)
    assert zeros == 0

    zeros = number_of_trailing_zeros(5)
    assert zeros == 1

    zeros = number_of_trailing_zeros(30)
    assert zeros == 7

    zeros = number_of_trailing_zeros(1099)
    assert zeros == 271