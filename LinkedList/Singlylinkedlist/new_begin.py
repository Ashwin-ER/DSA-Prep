class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            n=self.head
            while n is not None:
                print(n.data,"=>")
                n=n.next
    def add_begin(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
            
LL=linkedlist()
LL.add_begin(50)
LL.add_begin(10)
LL.display()
            
