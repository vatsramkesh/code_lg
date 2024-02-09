from typing import List

def insertion_sort(numbers: List[int]) -> List[int]:

    l = len(numbers)
    # Time O(n2), space O(1), but number os swap is less than what we do in bubble sort
    for i in range(1, l):
        temp = numbers[i]
        j = i-1
        while(j>=0 and temp < numbers[j]):
            numbers[j+1] = numbers[j]
            j-=1
        numbers[j+1] = temp

        # is_allowed = True
        # for j in range(i-1, -1, -1):
        #     if temp < numbers[j]:
        #         numbers[j+1] = numbers[j]
        #     else:
        #         numbers[j+1] = temp
        #         is_allowed = False
        #         break
        # if is_allowed:
        #     numbers[j] = temp
        
    return numbers

if __name__ == "__main__":
    assert insertion_sort([4, 3, 7, 1, 5]) == [1, 3, 4, 5, 7]
    assert insertion_sort([8, 4, 1, 5, 9, 2]) == [1, 2, 4, 5, 8, 9]