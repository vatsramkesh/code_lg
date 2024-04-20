"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
 where ⌊x⌋ denotes the largest integer less than or equal to x.
 For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:

    slow, fast = head, head
    prev = None
    if not head or not head.next:
        return None
    
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    
    prev.next = slow.next

    return head



        