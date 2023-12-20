"""
Check if given string is a palindrome string
"""

def is_palindrome(letter: str, left: int, right: int) -> bool:

    if left >= right:
        return True
    
    if letter[left] != letter[right]:
        return False

    return is_palindrome(letter, left+1, right-1)


def is_palindrome_str(letter: str) -> bool:
    l = len(letter)
    # Or simply letter == letter[::-1]
    if l &1:
        # odd len
        return letter[:l//2] == letter[l-1:l//2:-1]
    else:
        return letter[:l//2] == letter[l-1:l//2-1:-1]


if __name__ == "__main__":

    assert is_palindrome("racecar", 0, 6) == True
    assert is_palindrome("aba", 0, 2) == True
    assert is_palindrome("abcd", 0, 3) == False

    assert is_palindrome_str("racecar") == True
    assert is_palindrome_str("aba") == True
    assert is_palindrome_str("abcd") == False

