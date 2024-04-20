"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the index of
 the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Using two pointer Floyd's Tortoise/Detection & Hare algo
def has_cycle(head: ListNode) -> ListNode:
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None

def detect_first_node(head: ListNode) -> ListNode:
    meet = has_cycle(head)
    # Here has_cycle doesn't return the node where cycle start but will return where both pointers meet 
    # e.g 1 -> 2 -> 3-> 4 -> 5 -> 6 -> 3 in this case has_cycle will return node 5 this is where both pointers meet
    # So in this func now we need to detect the actual node where cycle start and concept if if we start from that 
    # meet node and head then both head and meet will catch at cycle node
    # TODO: to remove cycle just need to point the meet .prev node to null in this case point 6 to null, 
    # so need to keep prev pointer for meet 

    start = head
    # Logic is 
    while start != meet and meet:
        start = start.next
        meet = meet.next
    return start




def has_cycle_using_hash(head: ListNode) -> bool:
    # This use O(n) extra space to store occurance of node
    nodes_map = set()
    current = head
    while head:
        if current in nodes_map:
            return True
        nodes_map.add(current)
        current = current.next
    return False

