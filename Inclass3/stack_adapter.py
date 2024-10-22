from Queue_Example import Queue

class stack_adapter:

    def __init__(self):

       self.queue1 = Queue()

       self.queue2 = Queue()

 

    def push(self, item):
        self.queue1.enqueue(item)

    def pop(self):
        if self.queue1.is_empty():
            raise IndexError('The stack is empty')

        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        ret = self.queue1.dequeue()

        self.queue1 = self.queue2
        self.queue2 = self.queue1
        return ret

    def peek(self):
        if self.queue1.is_empty():
            raise IndexError('The stack is empty')
        
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        ret = self.queue1.dequeue()

        self.queue2.enqueue(ret)

        self.queue1 = self.queue2
        self.queue2 = self.queue1
        return ret
