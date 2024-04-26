"""
Given a linked list where in addition to the next pointer, each node has a child pointer, 
which may or may not point to a separate list. These child lists may have one or more children of their own,
 and so on, to produce a multilevel data structure, as shown in below figure. 
 You are given the head of the first level of the list. 
 Flatten the list so that all the nodes appear in a single-level linked list. 
You need to flatten the list in way that all nodes at the first level should come first, 
then nodes of second level, and so on.

Using extra space to hold child pointers
Approach1: Use a Queue and whenever we get a child/down node push it to queue and continue move forward
untill get to null, when we got to null, pop from queue and make next of current node(having next as null).

Approach2: The idea of solution is, we start from first level, process all nodes one by one, if a node has a child,
 then we append the child at the end of list, otherwise we don’t do anything. After the first level is processed, 
 all next level nodes will be appended after first level. Same process is followed for the appended nodes. 
"""

# A linked list node has data,  
# next pointer and child pointer  
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.child = None

# Return Node 
def newNode(data): 
    return Node(data) 

# The main function that flattens 
# a multilevel linked list 
# Since every node is visited at most twice, the time complexity is O(n) 
# where n is the number of nodes in given linked list.
def flattenlist(head): 
      
    # Base case 
    if not head: 
        return
      
    # Find tail node of first level linked list 
    temp = head 
    while(temp.next != None): 
        temp = temp.next
    currNode = head 
      
    # One by one traverse through all nodes  
    # of first level linked list 
    # till we reach the tail node  
    while(currNode != temp): 
          
        # If current node has a child 
        if(currNode.child): 
              
            # then append the child 
            # at the end of current list  
            temp.next = currNode.child 
              
            # and update the tail to new last node  
            tmp = currNode.child 
            while(tmp.next): 
                tmp = tmp.next
            temp = tmp 
              
        # Change current node  
        currNode = currNode.next
      


# A utility function to print  
# all nodes of a linked list  
def printList(head):  
    if not head:  
        return
    while(head):  
        print("{}".format(head.data), end = " ")  
        head = head.next


# Driver code  
if __name__=='__main__':  
      
    # Child list of 13 
    child13 = newNode(16) 
    child13.child = newNode(3) 
      
    # Child List of 10 
    head1 = newNode(4) 
    head1.next = newNode(20) 
    head1.next.child = newNode(2) #Child of 20 
    head1.next.next = newNode(13) 
    head1.next.next.child = child13 
      
    # Child of 9 
    child9 = newNode(19) 
    child9.next = newNode(15) 
  
    # Child List of 17 
    child17 = newNode(9) 
    child17.next = newNode(8) 
    child17.child = child9 
  
    # Child List of 7 
    head2 = newNode(17) 
    head2.next = newNode(6) 
    head2.child = child17 
      
    # Main List 
    head = newNode(10) 
    head.child = head1 
    head.next = newNode(5) 
    head.next.next = newNode(12) 
    head.next.next.next = newNode(7) 
    head.next.next.next.child = head2 
    head.next.next.next.next = newNode(11) 
  
    flattenlist(head) 
    # printList(head) 
