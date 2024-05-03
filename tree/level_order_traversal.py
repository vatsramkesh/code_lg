

"""
Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).
"""

from typing import List, Optional

from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return 0

    return max(max_depth(root.left), max_depth(root.right)) + 1

def print_level_order(root: Optional[TreeNode]):
    number_of_levels = max_depth(root)
    # Here time complexity is O(n*n)
    for level_number in range(1, number_of_levels+1):
        print_current_level(root, level_number)
        print()

    # In reverse order(leaf to root)
    for level_number in range(number_of_levels, 0, -1):
        print_current_level(root, level_number)
        print()


def print_current_level(root: Optional[TreeNode], level_number: int):
    if not root:
        return

    if level_number == 1:
        print(root.val, end=" ")
    elif level_number > 1:
        print_current_level(root.left, level_number-1)
        print_current_level(root.right, level_number-1)


def print_level_order_using_queue(root: Optional[TreeNode]):
    if not root:
        return
    q = Queue()
    q.put(root)
    data = []
    while not q.empty():
        item = q.get()
        data.append(item.val)
        if item.left:
            q.put(item.left)
        if item.right:
            q.put(item.right)
    return data


def print_level_order_using_queue_line_by_line(root: Optional[TreeNode]):
    if not root:
        return

    q = Queue()
    q.put(root)
    q.put(None)
    data = []
    level_data = []
    while not q.empty():
        item = q.get()
        if item == None:
            data.append(level_data)
            level_data = []
            if q.empty():
                return data
            
            q.put(None)
        else:
            level_data.append(item.val)
        if item and item.left:
            q.put(item.left)
        if item and item.right:
            q.put(item.right)
    return data


if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)

    assert max_depth(r) == 2
    print_level_order(r)
    assert print_level_order_using_queue(r) == [12, 98, 43]
    assert print_level_order_using_queue_line_by_line(r) == [[12], [98, 43]]
    
    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)

    assert max_depth(r) == 3
    print_level_order(r)

    r.left.right = TreeNode(99)
    
    assert print_level_order_using_queue(r) == [2, 4, 1, 7, 99, 8, 3]
    assert print_level_order_using_queue_line_by_line(r) == [[2], [4, 1], [7, 99, 8, 3]]
        