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
