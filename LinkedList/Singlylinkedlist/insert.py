class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.next

    def add_begin(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_mid(self, data, x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n=n.next
            if n is None:
                print("None")
            else:
                new_node = node(data)
                new_node.next = n.next
                n.next = new_node







LL = linkedlist()
LL.add_begin(50)
LL.add_end(100)
LL.add_mid(20,50)
LL.add_begin(10)
LL.display()
