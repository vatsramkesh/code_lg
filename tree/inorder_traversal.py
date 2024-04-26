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


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    output = []
    def traverse(root):
        if not root: return
        traverse(root.left)
        output.append(root.val)
        # print(output)
        traverse(root.right)

    traverse(root)
    return output

if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)

    assert inorderTraversal(r) == [98, 12, 43]

    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)

    assert inorderTraversal(r) == [7, 4, 2, 8, 1, 3]
    
        