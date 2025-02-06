class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, '=>', end='')
                temp=temp.next
            
L=singlelinkedlist()
n=node(10)
L.head=n
n1=node(20)
L.head.next=n1
L.display()
