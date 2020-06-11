# for Garbage collection 
import gc 

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
        cur_node = self.head

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def deleteNode(self, dele): 
          
        # Base Case 
        if self.head is None or dele is None: 
            return 
          
        # If node to be deleted is head node 
        if self.head == dele: 
            self.head = dele.next
  
        # Change next only if node to be deleted is NOT 
        # the last node 
        if dele.next is not None: 
            dele.next.prev = dele.prev 
      
        # Change prev only if node to be deleted is NOT  
        # the first node 
        if dele.prev is not None: 
            dele.prev.next = dele.next
        # Finally, free the memory occupied by dele 
        # Call python garbage collector 
        gc.collect() 
  


    def delete_node(self,data):
        cur_node = self.head

        while cur_node.data!=data:
            cur_node = cur_node.next
        if cur_node is self.head:
            cur_node.next.prev = None
            self.head = cur_node.next

        elif cur_node.next is None:
            cur_node.prev.next = None

        else:
            next_node = cur_node.next
            prev_node = cur_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
        

    def print_list(self):
        cur_node = self.head
        print ("forward list")
        while cur_node.next:
            print(cur_node.data,end=" ")
            cur_node = cur_node.next
        print (cur_node.data)

        print ("backward list")

        while cur_node:
            print(cur_node.data,end=" ")
            cur_node = cur_node.prev

            

l = dll()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.delete_node(3)
l.print_list()


# Driver program to test the above functions 
  
# Start with empty list 
dll = DoublyLinkedList() 
  
# Let us create the doubly linked list 10<->8<->4<->2 
dll.push(2); 
dll.push(4); 
dll.push(8); 
dll.push(10); 
  
print "\n Original Linked List", 
dll.printList(dll.head) 
  
# delete nodes from doubly linked list 
dll.deleteNode(dll.head) 
dll.deleteNode(dll.head.next) 
dll.deleteNode(dll.head.next) 
# Modified linked list will be NULL<-8->NULL 
print "\n Modified Linked List", 
dll.printList(dll.head) 
  
