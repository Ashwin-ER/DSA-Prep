
a=[7,4,51,6, 1,2,3]

temp = a[0]  
for i in range(len(a) - 1):
    a[i] = a[i + 1]
    #print(a[i],end=',')
a[len(a) - 1] = temp
#a.append(temp) #wrong
print(a)