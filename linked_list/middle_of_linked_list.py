"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Use two pointer slow and fast, slow will move 1 step and fast will move twice of slow(2 steps), 
so when fast reach end slow will be at middle of list
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head: ListNode) -> ListNode:

    slow, fast = head, head

    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    
    return slow


if __name__ == "__main__":

    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    assert middle_node(ll) == ll.next

    ll.next.next.next = ListNode(9)
    assert middle_node(ll) == ll.next.next