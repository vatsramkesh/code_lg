"""
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
 and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes
  inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def number_of_nodes(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return 0

    return number_of_nodes(root.left) + number_of_nodes(root.right)) + 1

if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)

    assert number_of_nodes(r) == 3
    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)

    assert number_of_nodes(r) == 6
        