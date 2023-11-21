# Find the only non-repeting element in an array where all other elements repeats exactly twice


def get_non_repeating(numbers: list[int]) -> int:
    
    
    """Using bit manipulation XOR of same number will always be zero and 
    then XOR of zero with any number will return that number
    Time complexity O(n)
    Execution: Think when same number came they cancel out each other so at last
    remaining number will be the one that is non-repeating
    
    0^5->5^4->5^4^1->5^4^1^3->5^4^1^3^4->5^1^3^1->5^3->5^3^5->3
    """
    res = 0

    for i in numbers:
        res = res^abs(i)

    return res

    # Using hash map, Time complexity O(n), Space complexity O(n)
    m = set()

    for i in numbers:
        if i not in m:
            m.add(i)
        else:
            m.remove(i)
    return list(m)[0]

    # using math sum and hash map Time complexity O(n), Space complexity O(n)
    arr_sum = sum(numbers)
    s = set()
    for n in numbers:
        s.add(n)
    set_sum = sum(s)
    return set_sum*2-arr_sum

if __name__ == "__main__":

    element = get_non_repeating([5, 4, 1, 3, 4, 1, 5])
    assert element == 3

    element = get_non_repeating([0, 4, 1, 3, -4, 1, 0])
    assert element == 3

