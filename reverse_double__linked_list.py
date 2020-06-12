class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

   # Function reverse a Doubly Linked List 
    def reverse(self): 
        temp = None
        current = self.head 
          
        # Swap next and prev for all nodes of  
        # doubly linked list 
        while current is not None: 
            temp = current.prev  
            current.prev = current.next
            current.next = temp 
            current = current.prev 
  
        # Before changing head, check for the cases like  
        # empty list and list with only one node 
        if temp is not None: 
            self.head = temp.prev

##    def reverse(self):
##        prev_node = None
##        cur_node = self.head
##
##        while cur_node:
##            next_node = cur_node.next
##            prev_node = cur_node.prev
##            cur_node.next = prev_node
##            cur_node.prev = next_node
##            prev_node = cur_node
##            cur_node = next_node
##
##        self.head = prev_node
##        
        


    def print_list(self):
        cur_node = self.head

        while cur_node.next:
            print(cur_node.data,end=" ")
            cur_node = cur_node.next
        print (cur_node.data)

        while cur_node:
            print(cur_node.data,end=" ")
            cur_node = cur_node.prev

l = dll()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.reverse()
l.print_list()
            
            
            
            
        
