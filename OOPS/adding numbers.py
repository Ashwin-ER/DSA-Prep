class subject:
    name=None
    age=None
    tam=None
    eng=None
    mat=None
    def total(self):
        print(self.tam+self.eng+self.mat)

marks = subject()
marks.tam=50
marks.eng=70
marks.mat=100
print(marks.total())


###22222
class node:
    name=None
    age=None
    def sentence(self):
        print(self.name+" is " + self.age +" years old")

node1 = node()
node1.name="ashwin"
node1.age='20'
node2=node()
node2.name="ash"
node2.age='15'
node1.sentence()
node2.sentence()
