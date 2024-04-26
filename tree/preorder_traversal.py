"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

This problem seems to be asking for performing an preorder traversal of a 
binary tree, which visits the nodes in the order: root, left, right.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    output = []
    def traverse(root):
        if not root: return
        output.append(root.val)
        traverse(root.left)
        traverse(root.right)

    traverse(root)
    return output

if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)

    assert preorderTraversal(r) == [12, 98, 43]

    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)

    assert preorderTraversal(r) == [2, 4, 7, 1, 8, 3]