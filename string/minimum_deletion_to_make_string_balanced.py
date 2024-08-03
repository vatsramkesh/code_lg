"""
You are given a string s consisting only of characters 'a' and 'b'​​​​.
You can delete any number of characters in s to make s balanced. s is balanced 
if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

"""

def minimum_deletion_optimized(input_str: str) -> int:

    b_count = 0
    min_deletion = 0

    for char in input_str:
        if char == "a":
            min_deletion = min(min_deletion+1, b_count)
        else:
            b_count+=1

    return min_deletion

def minimum_deletion(input_str: str) -> int:

    # number_of_a_to_the_right = [0]*len(input_str)
    if len(s) < 2:
        return 0

    a_count_right = [0] * len(input_str)

    for i in range(len(input_str)-2, -1, -1):
        a_count_right[i] = a_count_right[i+1]
        if input_str[i+1] == "a":
            a_count_right[i]+=1
    # print(a_count_right)
        
    b_count_left = 0

    min_deletion = len(input_str)

    for i in range(1, len(input_str)):
        if input_str[i-1] == "b":
            b_count_left+=1

        min_deletion = min(min_deletion, (b_count_left+a_count_right[i]))
    return min_deletion


if __name__ == "__main__":

    assert minimum_deletion_optimized("bbaaaaabb") == 2
    assert minimum_deletion_optimized("aababbab") == 2
    assert minimum_deletion_optimized("a") == 0
    assert minimum_deletion_optimized("bbbbbbbbbbbbbb") == 0

