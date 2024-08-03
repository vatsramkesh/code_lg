"""
Given the root of a binary tree, return its diameter.

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

def get_tree_diameter(root: Optional[TreeNode]) -> int:
    ans = [0]
    
    def get_diameter(root: Optional[TreeNode]) -> int:
        # nonlocal ans
        if not root:
            return -1

        lh = get_diameter(root.left)
        rh = get_diameter(root.right)
        ans[0] = max(ans[0], lh+rh+2)
        return 1 + max(lh, rh)

    get_diameter(root)
    return ans[0]


if __name__ == "__main__":
    r = TreeNode(3)
    r.left = TreeNode(2)
    r.left.left = TreeNode(7)
    r.right = TreeNode(4)
    assert get_tree_diameter(r) == 3
    r.right.left = TreeNode(1)
    r.right.right = TreeNode(5)
    assert get_tree_diameter(r) == 4