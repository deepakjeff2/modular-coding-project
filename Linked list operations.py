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
 def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.add_end(data)
    
    def count_length(self):
        count = 0
        n = self.head
        while n:
            count+=1
            n = n.ref
        return count
    
    def remove_at(self,index):
        if index < 0 or index >= self.count_length():
            raise Exception('invalid input')
        
        if index == 0:
            self.head = self.head.ref
            return
        
        count = 0
        n = self.head
        while n:
            if count == index-1:
                n.ref = n.ref.ref 
                break
                
            n = n.ref
            count+=1

    def insert_at(self,data,index):
        if index < 0 or index >= self.count_length():
            raise Exception('invalid index')
            
        if index == 0:
            self.add_begin(data)
            return
        
        count = 0
        n = self.head
        while n:
            if count == index-1:
                node = Node(data)
                node.ref = n.ref
                n.ref = node
            n = n.ref
            count+=1

    def inser_after(self,data_after,data):
        n = self.head
        while n:
            if data_after == n.data:
                node = Node(data)
                node.ref = n.ref
                n.ref = node
                break
                
            n = n.ref
    
    def remove_by_value(self,data):
        n = self.head
        while n:
            if data == n.ref.data:
                n.ref = n.ref.ref
                break
            n = n.ref
            
            
if __name__ == '__main__':       
    lis = Linkedlist()
    lis.add_begin('hello')
    lis.add_end('world')
    lis.print_ll()
    pass          
