"""
Implement stack using Linked List.
Implement push, pop and peak functions
"""

class Node:

    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, element):

        temp = self.head
        self.head = Node(element, temp)
        
        self.size+=1
    
    def pop(self):
        if not self.head:
            raise Exception("Stack is underflow, no element to pop")
        
        res = self.head.val
        self.head = self.head.next
        
        self.size-=1
        return res
    
    def peak(self):
        if not self.head:
            raise Exception("Stack is underflow, no element to pop")
        
        return self.head.val

    def get_size(self):
        return self.size


if __name__ == "__main__":
    s = Stack()
    s.push(9)
    s.push(6)
    assert s.peak() == 6
    assert s.pop() == 6
    s.push(87)
    s.push(65)
    s.push(54)
    assert s.pop() == 54
    s.push(19)
    s.push(99)
    s.push(65) # This Should raise oberf:q
     