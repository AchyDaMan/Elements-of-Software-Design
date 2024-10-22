import sys
#Link defines the list
class Link(object):
    ''' This class represents a link between data items only.'''
    def __init__ (self, data, next_link = None):
        self.data = data
        self.next = next_link
    #Print the data!
    def print_data(self):
        ''' Print the data contained in this link.'''
        print(self.data)
    # Print!
    def __str__(self):
        return str(self.data) + " --> " + str(self.next)

# The circular LinkedList class
class CircularList(object):
    # Constructor
    def __init__ (self):
        self.first = None

    # Insert an element (value) in the list
    def insert (self, data):
        new_link = Link(data)
        # insert the first element
        if self.first is None:
            self.first = new_link
            new_link.next = self.first
        else:
          node = self.first
          while node.next != self.first:
              node = node.next

          node.next = new_link
          new_link.next = self.first


    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find (self, data):
        if self.first is None:
            return None
        else:
            node = self.first
            while True:
                if node.data == data:
                    return node 
                node = node.next
                if node == self.first:
                    break  
            return None


        
    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete (self, data):
        if self.first is None:
            return None
        node = self.first
        prev = None
        
        while True:
            if node.data == data:
                if prev:
                    prev.next = node.next
                else:
                    temp = self.first
                    while temp.next != self.first:
                        temp = temp.next
                    temp.next = node.next
                    self.first = node.next
                
                return
            
            prev = node
            node = node.next
            
            if node == self.first:
                break
                

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after (self, start, n):
        if not self.first:
            return None, None

        node = start
        prev = None
        
        # Move to the nth link
        for _ in range(n):
            prev = node
            node = node.next
            if node == self.first:
                break

        # Delete the nth link
        if prev is not None:
            prev.next = node.next
        if node == self.first:
            # Update first if we're deleting the start
            temp = self.first
            while temp.next != self.first:
                temp = temp.next
            temp.next = node.next
            self.first = node.next

        return node.data, node.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if not self.first:
            return 'List is empty'

        result = []
        node = self.first
        while True:
            result.append(str(node.data))
            node = node.next
            if node == self.first:
                break

        return ' -> '.join(result)


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # Do the actual josephus problem
    list = CircularList()

    for i in range(num_soldiers):
        list.insert(i)

    order = []
    current = list.first

    while list.first and list.first.next != list.first:
        for _ in range(elim_num - 1):
            current = current.next
        order.append(current.data)
        current = current.next
        list.delete(order[-1])

    order.append(list.first.data)  # The last remaining man
    for soldier in order:
        print(soldier+1)

if __name__ == "__main__":
  main()
