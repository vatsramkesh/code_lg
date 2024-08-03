"""
Given the root of a complete binary tree, Create doublee linked list out of it and return the
head of linked list.
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    output = []
    # Here it is using O(n) extra space to store inorder traversal
    def traversal(root: Optional[TreeNode]):
        if not root:
            return
        traversal(root.left)
        output.append(root.val)
        traversal(root.right)
    traversal(root)
    return output

def binary_tree_to_doublee_ll(root: Optional[TreeNode]):
    tree_nodes = inorder_traversal(root)
    head = Node(tree_nodes[0])
    temp = head
    for i, v in enumerate(tree_nodes[1:]):
        n = Node(v)
        head.next = n
        n.prev = head
        head = n
    return temp 

class TreeToLinkedList:

    def __init__(self):
        self.prev_node = None
        self.head_node = None

    def binary_tree_to_doublee_ll_inplace(self, root: Optional[TreeNode]):
        # prev_node = None
        # head_node = None

        def create_ll(root: Optional[TreeNode]):
            if not root:
                return
            
            create_ll(root.left)

            if not self.head_node:
                self.head_node = root
            else:
                root.left = self.prev_node
                self.prev_node.right = root

            self.prev_node = root
            create_ll(root.right)
        
        create_ll(root)
        return self.head_node


def print_ll(head: Optional[Node]):

    while head.next:
        print("CURRENT: ", head.val)
        print("NEXT: ", head.next.val)
        if head.prev:
            print("PREV: ", head.prev.val)
        head = head.next


if __name__ == "__main__":
    r = TreeNode(12)
    r.left = TreeNode(98)
    r.right = TreeNode(43)
    head = binary_tree_to_doublee_ll(r)
    print_ll(head)
    t = TreeToLinkedList()
    h = t.binary_tree_to_doublee_ll_inplace(r)
    # print(inorder_traversal(h))
    # assert number_of_nodes(r) == 3

    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)
    head = binary_tree_to_doublee_ll(r)
    print_ll(head)
    # assert number_of_nodes(r) == 6

    r = TreeNode(2)
    r.left = TreeNode(4)
    r.left.left = TreeNode(7)
    r.right = TreeNode(1)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(3)

    t = TreeToLinkedList()
    h = t.binary_tree_to_doublee_ll_inplace(r)
    assert h.val == 7
    assert h.right.val ==  4
    assert h.right.left.val ==  7
    assert h.right.right.val ==  2
        