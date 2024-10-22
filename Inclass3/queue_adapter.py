
from Stack_Example import Stack

class queue_adapter:

    def __init__(self):

       self.stack1=Stack()

       self.stack2=Stack()

 
    def enqueue(self, item):
       self.stack1.push(item)
 
    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        if self.stack2.is_empty():
            raise IndexError("dequeue from empty queue")
        
        return self.stack2.pop()
       