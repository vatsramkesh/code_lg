
"""
Print top/bottom view tree.

Given the root of a binary tree, imagine yourself standing on the top/bottom of it, 
return the values of the nodes you can see ordered from top or bottom.

Approach 1: While doing level order traversal we start with root and while pushing to queue, push a tuple 
containing reference of node position with respect to root node(if left to root do -1 and right to root +1)
and node(postition, node).
For top view create a hash map and poll the queue, if current poll item(position reference) isn't in hash_map
add it to hash_map and continue pusging its left and right to queue along with its reference position.
So doing this at a time there will be only one item in hash_map for 1 position and we arn't updating map so 
that item visible from top(top to bottom) doesn;t get overrride. then for ordering sort the hash_map by
keys or can used orderdict.


For bottom view just remove if condition so we keep overriding map.
"""
from typing import List, Optional

from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_top_view_of_binary_tree(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
        
    nodes_q = Queue()
    nodes_q.put((0, root))
    level_map = {}

    while not nodes_q.empty():
        current_node = nodes_q.get()
        if not level_map.get(current_node[0]):
            level_map[current_node[0]] = current_node[1].val
        
        if current_node: 
            if current_node[1].left:
                nodes_q.put((current_node[0] -1, current_node[1].left))
            if current_node[1].right:
                nodes_q.put((current_node[0] + 1, current_node[1].right))

    level_map = sorted(level_map.items())
    return [i[1] for i in level_map]


def print_bottom_view_of_binary_tree(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
        
    nodes_q = Queue()
    nodes_q.put((0, root))
    level_map = {}

    while not nodes_q.empty():
        current_node = nodes_q.get()
        level_map[current_node[0]] = current_node[1].val
        
        if current_node: 
            if current_node[1].left:
                nodes_q.put((current_node[0] -1, current_node[1].left))
            if current_node[1].right:
                nodes_q.put((current_node[0] + 1, current_node[1].right))

    level_map = sorted(level_map.items())
    return [i[1] for i in level_map]




if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)

    assert print_top_view_of_binary_tree(r) == [98, 12, 43]
    assert print_bottom_view_of_binary_tree(r) == [98, 12, 43]
    
    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)
    r.left.right = TreeNode(99)
    
    assert print_top_view_of_binary_tree(r) == [7, 4, 2, 1, 3]
    assert print_bottom_view_of_binary_tree(r) == [7, 4, 8, 1, 3]

    r = TreeNode(6)
    r.left = TreeNode(2)
    # r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    # r.right.left = TreeNode(8)
    r.right.right = TreeNode(5)
    r.left.right = TreeNode(3)
    r.left.right.right = TreeNode(4)
    
    assert print_top_view_of_binary_tree(r) == [2, 6, 1, 5]
    assert print_bottom_view_of_binary_tree(r) == [2, 3, 4, 5]

    # root_node = TreeNode
        