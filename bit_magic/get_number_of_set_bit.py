# Count the number of 1 in binary

def get_set_bit(n: int) -> int:

    count = 0

    while n: # O(log n) n- number of bits
        if n & 1:  # Check LSB
            count += 1
        n = n >> 1 # shift right by 1 so all 1's keep coming on LSB and replaced 0 untill all bits 0
        
    return count

    while n > 0: # O(log n) n- number of bits
        if n % 2:
            count +=1
        n //=2
        
    return count

    while n: # O(number of set 1 bits) so  is optimized
        # Using bit manipulation n = 1011 & 1010 = 1010 (always remove right most 1 (LSB) in each operation so count the steps )
        n = n & (n-1) 
        count += 1
    return count


if __name__ == "__main__":
    bit = get_set_bit(4)
    assert bit == 1

    bit = get_set_bit(9)
    assert bit == 2

    bit = get_set_bit(31)
    assert bit == 5

    # Note: To find number of bits in binary rerp of number n -> (log n) + 1