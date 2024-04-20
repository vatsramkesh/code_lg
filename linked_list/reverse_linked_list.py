"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode) -> ListNode:
    current = head
    prev = None

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

def reverse_linked_list_recursive(head: ListNode) -> ListNode:

    if not head or not head.next:
        return head

    new_head = reverse_linked_list_recursive(head.next) 
    """ This return new head of reverse linked list 
    but link between prev node and new ists last node is broken
    So if list is :
    1 -> 2 -> 3 -> 4
    output from above reverse_linked_list_recursive call will be:
    4 -> 3 -> 2   1
    We just have to link 1 and 2 node and we have
    head pointing to 1 already and head.next is still point to 2, so we just need to reverse this link
    """
    head_next = head.next
    head_next.next = head
    head.next = None

    return new_head