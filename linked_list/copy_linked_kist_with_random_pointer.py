"""
A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state. None of the pointers 
in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then 
for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null
 if it does not point to any node.
Your code will only be given the head of the original linked list.
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # This algo do two interationand usinh O(n) extras space for storing mapping
        
        if not head:
            return None

        # Adding None to remove if conditions for next and random node check
        new_old_mapping = {None: None}
        current = head

        while current:
            # Here just create new Node without any link and keep mapping in map 
            # so that we can use them in next iteration for doing linking
            new_old_mapping[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            # Here fetch from map and do linking
            copied_node = new_old_mapping[current]
            copied_node.next = new_old_mapping[current.next]
            copied_node.random = new_old_mapping[current.random]
            current = current.next
        return new_old_mapping[head]

def copy_random_list_with_constant_space(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # This algo do two interationand usinh O(n) extras space for storing mapping
        
        if not head:
            return None

        # Adding None to remove if conditions for next and random node check
        new_old_mapping = {None: None}
        current = head

        # In serting new node in between
        while current:
            temp = current.next
            copied_node = Node(current.val)
            current.next = copied_node
            copied_node.next = temp
            current = temp

        # Setting random pointer for new nodes
        current = head
        while current:
            if current.next and current.random:
                current.next.random = current.random.next
        
        current = head
        while current:
            # Here fetch from map and do linking
            copied_node = new_old_mapping[current]
            copied_node.next = new_old_mapping[current.next]
            copied_node.random = new_old_mapping[current.random]
            current = current.next
        return new_old_mapping[head]

