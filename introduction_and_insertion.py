class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self,data):
        new_node = node(data)
        cur_node = self.head

        if self.head is None:
            self.head = new_node
            return

##        if self.head is None:
##            self.push(data)
##            return
        while cur_node.next!=None:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node

    def insert_after(self,data,item):
        new_node = node(data)
        cur_node = self.head

        while cur_node.data!=item:
            cur_node = cur_node.next
        next_node = cur_node.next
        if next_node:
            cur_node.next = new_node
            new_node.next = next_node
            new_node.prev = cur_node
            next_node.prev = new_node
        else:
            self.append(data)
            
        
    def print_list(self):
        cur_node = self.head
        print ("\nTraversal in forward direction")
        while cur_node.next:
            
            print(cur_node.data,end=" ")
            cur_node = cur_node.next
        print (cur_node.data)

        print ("\nTraversal in reverse direction")
        while cur_node:
            
            print (cur_node.data,end=" ")
            cur_node = cur_node.prev

        
l = dll()
l.append(6)
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.insert_after(7,6)

l.print_list()
            
        
        
