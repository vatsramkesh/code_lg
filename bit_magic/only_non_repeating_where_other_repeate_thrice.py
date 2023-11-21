# Find the only non-repeating element in an array where every other elements repeate thrice(or k time)

def get_non_repeating(numbers: list[int], k: int) -> int:
    numbers.sort() # Nlog(N)
    a = 1
    if len(numbers) < k:
        return numbers[0]
    elif numbers[0] != numbers[1]:
        return numbers[0]
    elif numbers[-1] != numbers[-2]:
        return numbers[-1]
    
    
    while a < len(numbers):
        if numbers[a] != numbers[a-1]:
            return numbers[a-1]
        a+=k 

    # return 

if __name__ == "__main__":

    element = get_non_repeating([5, 4, 1, 3, 4, 1, 5, 5, 4, 1], 3)
    assert element == 3

    element = get_non_repeating([9, 8, 8, 8, 8, 5, 5, 5, 5], 4)
    assert element == 9