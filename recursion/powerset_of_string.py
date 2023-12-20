"""
Print power set for a given string
"""


def powerset(letter:str, indx: int, current: str) -> None:

    if len(letter) == indx:
        print(current)
        return
    # here time complexity is O(2 power n) 
    powerset(letter, indx+1, current + letter[indx])
    powerset(letter, indx+1, current)

# Iterative methode algo

# Create an initially empty list L which will eventually represent the powerset
# For each element, give it an index, ranging from 0 to n-1.
# Suppose we have {A, B, C}. Let the index of A be 0, B be 1, C be 2.
# Loop through all the numbers from 0 to 2n-1 and express each in binary form.
# The loop counter i goes from 0 (000 in binary) to 7 (111 in binary).
# Create a subset Ti based on the binary number, which contains the elements such that the binary digit position of the elements' index for i is 1.
# The ones digit is given position 0, the fours digit (third digit) is given position 2.
# When we have 0, the subset T0 is the empty set.
# When we have 5, the binary digits are 101, the digits with position 2 and 0 are ones, and so the subset T5 is {A, C}.
# Add that subset to the original list L.

if __name__ == "__main__":
    powerset("abc", 0, "")