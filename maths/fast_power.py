"""Calculate a to power b fast"""


def fast_power(a: int, b: int) -> int:

    res = 1
    # Here time complexity is log(b) as dividing b by 2 each iterartion
    while b > 0:
        if b&1: # if b is odd we can say a to b = a * a to (b-1)
            res = res * a
        a = a * a
        print(a, b)
        b = b >> 1 # a ki b can be a ki 2 ki b//2, so here dividing b by 2 using right shift 
    return res


if __name__ == "__main__":
    # print(fast_power(33, 35) )
    assert fast_power(3, 5) == 243
    # assert fast_power(1, 10) == 1