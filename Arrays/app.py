

a = [3,1,2,2,5,4,5,6,6]

#SORTING AND REMOVING DUPLICATES
b = sorted(a)
k=[]
for i in b:
    if i not in k:
        k.append(i)
print(k)
print(k[-2])




print(set(sorted(a)))


#c = set(sorted(a))
c = sorted(set(a))
print(c[-2])



#USING FOR LOOP

a = [3,1,2,2,5,4,5,6,6]
max=a[0] #LARGEST NUMBER
for i in a:
    if i>max:
        max=i
        #i=i+1
print(max)

second_max = a[0] #SECOND LARGEST NUMBER
for i in a:
    if i>second_max and i<max:
        second_max=i
print(second_max)

