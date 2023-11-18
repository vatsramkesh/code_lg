
def set_bit(n: int, k: int) ->int :
    mask = 1
    mask = mask << k # left shift 1 by k bit, if k = 3 then mask will be 00000100
    return n | mask

if __name__ == "__main__":
    bit = set_bit(10, 2)
    assert bit == 14

    bit = set_bit(15, 3)
    assert bit == 15
