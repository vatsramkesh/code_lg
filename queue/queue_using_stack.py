"""
Implement Queue using two Stack
"""

class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    """
    Algo: Keep two stanck/Python list
    always push to s1
    while do pop we need the item that was pushed first, so first pop all alement from s1
    and push them to s2, now they will be reversed(one we inseted fiest will be at top of stack), so pop 
    the top and keep store at result, then again move back all elements from s2 to s1.
    Return the result
    """
    # O(1)
    def push(self, data):
        s1.append(data)

    # O(n)
    def pop(self):
        while self.s1:
            self.s2.append((self.s1.pop())
        res = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return res

"""
Similarly we can implement Stack using two queue, here push will be O(n), keep pop from q1 while get empty
and push to q2 then once q1 get empty add the new element in q1 and then again move back all elements from q2 to q1
"""