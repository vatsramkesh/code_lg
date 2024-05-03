"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.
"""

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

This problem seems to be asking for performing an inorder traversal of a 
binary tree, which visits the nodes in the order: left, root, right.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return 0

    return max(max_depth(root.left), max_depth(root.right)) + 1

if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)

    assert max_depth(r) == 2
    r = TreeNode(2)
    r.left = TreeNode(4)
    # r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    # r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)

    assert max_depth(r) == 3
        