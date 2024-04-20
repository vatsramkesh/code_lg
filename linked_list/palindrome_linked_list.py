"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
"""
from middle_of_linked_list import middle_node
from reverse_linked_list import reverse_linked_list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head: ListNode) -> bool:

    # if not head or not head.next:
    #     return True

    # mid = middle_node(head)
    # print(mid.val)
    # last = reverse_linked_list(mid.next)
    # current = head
    # while last:

    #     if last.val != current.val:
    #         return False
    #     last = last.next
    #     current = current.next
    # return True

    slow, fast = head, head
    prev = None
    # Reverse first half and finding the middle at one go
    while fast and fast.next:
        fast = fast.next.next
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    if fast:
        slow = slow.next

    while prev:
        if prev.val != slow.val:
            return False
        prev = prev.next
        slow = slow.next
    return True


    # Using O(n) extra space
    if not head or not head.next:
        return True
    newHead = ListNode(head.val)
    
    start = head.next
    while start:
        n = ListNode(start.val)
        n.next = newHead
        newHead = n
        start = start.next
        
    while newHead:
        if newHead.val != head.val:
            return False
        else:
            newHead = newHead.next
            head = head.next
    return True
        

    # Using stack O(n/2) extra space
        
    slow = fast= cur = head
    while fast and fast.next:
        fast = fast.next.next
        
        slow = slow.next
        
    # Second half in stack
    st = []
    while slow:
        st.append(slow.val)
        
        slow = slow.next
    
    while st:
        if st.pop() != cur.val:
            return False
        cur = cur.next
    return True


if __name__ == "__main__":

    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(1)
    assert is_palindrome(ll) == True
    

    ll.next.next.next = ListNode(1)
    assert is_palindrome(ll) == False

    ll.next.next.next.next = ListNode(2)
    ll.next.next.next.next.next = ListNode(1)
    assert is_palindrome(ll) == True