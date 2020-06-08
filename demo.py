class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class cll:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        cur_node = self.head
        if self.head:
            while cur_node.next!=self.head:
                cur_node = cur_node.next
            new_node.next = self.head
            cur_node.next = new_node
            self.head = new_node
        else:
            self.head = new_node
            new_node.next = self.head

    def print_list(self):
        cur_node = self.head

        while cur_node.next!=self.head:
            print(cur_node.data)
            cur_node = cur_node.next
        print(cur_node.data)

l = cll()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.push(0)
l.print_list()
        
