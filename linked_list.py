class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
          
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
          
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
        
    def print_list(self):
        if self.head is None:
            return []
        nodes = []
        itr = self.head
        while itr:
            nodes.append(str(itr.data))
            itr = itr.next
        return nodes
                                
    def remove_beginning(self):
        if self.head is None:
            print('Empty Linked List')
            return
            
        none_do_remove = self.head
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
    def remove_at_end(self):
        if self.head is None:
            print('Empty Linked List')
            return     
           
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
            
        current_node = self.head
        
        while current_node.next != self.tail:
            current_node = current_node.next
            
        self.tail = current_node
        
        self.tail.next = None
        
    def remove_at(self, index):
        if index<0:
            raise Exception("Invalid Index. Please input correct index number.")
        
        if index==0:
            self.head = self.head.next
            return
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
                
            itr = itr.next
            count += 1