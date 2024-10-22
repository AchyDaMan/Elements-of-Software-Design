from LL_Example import LinkedList

 

class stack_adapter2:

    def __init__(self):
       self.list=LinkedList()


    def push(self, item):
        self.list.insert_first(item)

    def pop(self):

        item = self.list.first.data
        
        self.list.delete_link(item)

 

    def peek(self):