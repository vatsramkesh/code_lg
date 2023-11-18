
def get_bit(n: int, k: int) -> int:
    mask = 1
    mask = mask << k # left shift 1 by k bit, if k = 3 then mask will be 00000100
    # print(n & mask)
    return n & mask

if __name__ == "__main__":
    bit = get_bit(4, 0)
    assert bit == 0

    bit = get_bit(4, 2)
    assert bit != 0

    bit = get_bit(500, 3)
    assert bit == 0