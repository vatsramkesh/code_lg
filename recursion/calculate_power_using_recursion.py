"""Find power of a number using recyrsion """


def get_power(a: int, b: int) -> int:

    if b == 1: # base case
        return a
    # relation between problem and sub problem is if I know a to b-1 then I can find a to b
    # i.e a to b = a * a to b-1
    return a * get_power(a, b-1) 


if __name__ == "__main__":
    assert get_power(3, 5) == 243
    assert get_power(1, 9) == 1