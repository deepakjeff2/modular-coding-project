class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def print_ll(self):
        if self.head is None:
            print('linkedlist is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,end='-->')
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
            
if __name__ == '__main__':       
    lis = Linkedlist()
    lis.add_begin('hello')
    lis.add_end('world')
    lis.print_ll()
    pass          
