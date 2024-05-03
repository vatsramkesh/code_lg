"""
Given the root of a complete binary tree, return the the node with max val in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
 and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes
  inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""


import math
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_value_node(root: Optional[TreeNode]) -> List[int]:

    def helper(root, max_val):
        if not root:
            return max_val
        if not root.left and not root.right:
            return root.val
        return max(helper(root.left, max_val), helper(root.right, max_val), max_val)

    return helper(root, 0)

# Time complexity O(n)
# Space complexity O(h)
def max_node_value(root: Optional[TreeNode]) -> List[int]:

    if not root:
        return -math.inf
    return max(root.val, max_node_value(root.left), max_node_value(root.right))

    # return helper(root, 0)

if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)

    assert max_value_node(r) == 98
    assert max_node_value(r) == 98
    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)

    assert max_value_node(r) == 8
    assert max_node_value(r) == 8
        