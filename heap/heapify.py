from typing import List

def heapify(numbers: List, item_index: int, numbers_len: int):
    largest = item_index
    l_chield_index = 2*item_index +1
    r_chield_index = l_chield_index + 1
    if l_chield_index < numbers_len and numbers[largest] < numbers[l_chield_index]:
        largest = l_chield_index
    if r_chield_index < numbers_len and numbers[largest] < numbers[r_chield_index]:
        largest = r_chield_index
    
    if largest != item_index:
        numbers[largest], numbers[item_index] = numbers[item_index], numbers[largest]
        heapify(numbers, largest, numbers_len)


def insert_in_heap(numbers: List, val: int):
    numbers.append(val)
    l = len(numbers)

    while(l>1):
        parent = (l//2)-1
        if numbers[parent] < numbers[l-1]:
            numbers[parent], numbers[l-1] = numbers[l-1], numbers[parent]
        l = l//2


# def remove_from_heap(numbers: List[int]):
#     largest = numbers[0]
#     n = len(numbers)
#     numbers[0] = numbers[n-1]
#     n = n-1
#     heapify(numbers, 0, n-1)


def build_heap(numbers: List[int]):
    n = len(numbers)
    # Since its(heap) is a complete binary tree, we can safely say half of its nodes(n//2)
    # are leaf node and since they doesn't have chield we can say they satisfy heap algo.
    # So just need to run heapify for 0-n//2 nodes in reverse order, it will make sure all
    # the nodes/tree below that follow heapify property
    # So here time complexity would be O(n) vs traditional way where we start 
    # from stract then iterate and compare an build heap with take O(n log n)
    for i in range(n//2, -1, -1):
        heapify(numbers, i, n)

    # Linear/Triditional way this is O(n log n), here n by current loop and log n in insert_in_heap
    # heap = [numbers[0]]
    # for i in range(1, n):
    #     heapifinsert_in_heapy_1(heap, numbers[i])


if __name__ == "__main__":
    nums = [10, 30, 50, 20, 35, 15, 90]
    build_heap(nums)
    print(nums)
    