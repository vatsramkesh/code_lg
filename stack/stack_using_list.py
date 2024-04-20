"""
Implement stack using Python list.
Implement push, pop and peak functions
"""

class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = [None] * capacity
        self.top = -1

    def push(self, element):
        if self.top == self.capacity-1:
            raise Exception(f"Stack is overflow with capacity: {self.capacity}")
        
        self.top+=1
        self.elements[self.top] = element
    
    def pop(self):
        if self.top == -1:
            raise Exception("Stack is underflow, no element to pop")
        
        element = self.elements[self.top]
        self.top -=1
        return element
    
    def peak(self):
        return self.elements[self.top]


if __name__ == "__main__":
    s = Stack(5)
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
    # s.push(65) # This Should raise overflow
     