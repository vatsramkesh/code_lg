
def number_of_ops(number_1: int, number_2: int) -> int:

    number_1 = number_1 ^ number_2 # Will set 1 only for different bits

    return get_number_of_set_bits(number_1)

def get_number_of_set_bits(number: int) -> int:

    count = 0
    while number:
        number = number & (number - 1)
        count +=1
    return count

if __name__ == "__main__":

    number_1 = 22 # 10110
    number_2 = 27 # 11011
    bit = number_of_ops(number_1, number_2)
    assert bit == 3

    number_1 = 2 # 10
    number_2 = 31 # 11111
    bit = number_of_ops(number_1, number_2)
    assert bit == 4

    number_1 = 8 # 1000
    number_2 = 1 # 1
    bit = number_of_ops(number_1, number_2)
    assert bit == 2

    number_1 = 31 # 11111
    number_2 = 31 # 11111
    bit = number_of_ops(number_1, number_2)
    assert bit == 0

