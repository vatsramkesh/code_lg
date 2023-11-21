
def clear_bit(N: int, K: int) -> int:

    mask = ~(1<<K)

    return N & mask


if __name__ == "__main__":
    bit = clear_bit(13, 2)
    assert bit == 9

    bit = clear_bit(996, 7)
    assert bit == 996
