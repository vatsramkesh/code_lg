
class PythonQueue:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.queue = [] # FIFO

    
    def enqueue(self, data):

        # Check queue isn't full
        if (self.rear+1)%self.capacity == self.front:
            raise Exception(f"Queue with capacity {self.capacity} is full")
        
        self.rear = (self.rear+1)%self.capacity 
        self.queue[self.rear] = data
        # To handle when queue is empty and adding first item so updating front as well from -1 to 0
        if self.front == -1:
            self.front = 0

    def dequeue(self):
        if self.front == -1:
            raise Exception("Queue is empty, cann't dequeue item")
        result = self.queue[self.front]

        # To handle when we have only 1 item in queue set both front and rear -1(like new queue)
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1)%self.capacity
        
        return result
    

# if __name__ == "__main__":

