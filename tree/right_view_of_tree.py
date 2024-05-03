
"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
Print right side of tree.
Approach 1: While doing level order traversal we were adding right node at index -1 of every level
and index -1 will be right most node of that level i.e output from level order traversal look like
[[12, 13], [87, 54, 98, 54], [9, 88, 65]] then [13, 54, 65] should be the right nodes view.
So do level order traversal and return the 1st index for every level.
Arroach 2: Create a dict with level_number as key and values should be nodes at that level, but only add node
to a level if its not there in dict in that we will always see the right node overriding valus at level
"""
from typing import List, Optional

from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_right_view_of_tree_using_level_order_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
        
    nodes_q = Queue()
    nodes_q.put(root)
    nodes_q.put(None)
    output = []
    level_items = []
    while not nodes_q.empty():
        current_node = nodes_q.get()
        if not current_node:
            # Index -1 is right most index for a level
            if len(level_items) > 0:
                output.append(level_items[-1])
            level_items = []
            if nodes_q.empty():
                return output
            nodes_q.put(None)
        else:
            level_items.append(current_node.val)
        if current_node: 
            if current_node.left:
                nodes_q.put(current_node.left)
            if current_node.right:
                nodes_q.put(current_node.right)

    return output


def print_right_view_of_tree(root: Optional[TreeNode]):
    # Time and space complexity are O(n) here
    output_hash = {}
    print_right_view_util(root, output_hash, 0)
    return list(output_hash.values())


def print_right_view_util(root: Optional[TreeNode], output_hash: dict, level_number: int):

    if not root:
        return
    
    # if not output_hash.get(level_number):
    output_hash[level_number] = root.val
    print_right_view_util(root.left, output_hash, level_number+1)
    print_right_view_util(root.right, output_hash, level_number+1)




if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)

    assert print_right_view_of_tree(r) == [12, 43]
    
    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)
    r.left.right = TreeNode(99)
    
    assert print_right_view_of_tree(r) == [2, 1, 3]

    # root_node = TreeNode
        