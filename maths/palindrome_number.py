""" Check given number is a valid palindrome
"""


def is_palindrome(n: int) -> bool:
    
    return n == get_reverse_number(n)

def get_reverse_number(n: int) -> int:

    num = 0

    while n > 0:
        num = num*10 + n%10
        n= n//10
    return num


if __name__ == "__main__":
    assert is_palindrome(3) == True

    assert is_palindrome(1991) == True
    
    assert is_palindrome(198) == False

    assert is_palindrome(-1991) == False
