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
        
    def remove_at(self, data):
        if self.head is None:
            return None
            
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            
            if self.head is None:
                self.tail = None 
                
            return removed_data
            
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                removed_data = current_node.next.data
                
                if current_node.next == self.tail:
                    self.tail = current_node
                    
                current_node.next = current_node.next.next
                return removed_data
                
            current_node = current_node.next
            
        return None
