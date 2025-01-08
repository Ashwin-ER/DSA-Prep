a = [0, 1, 2, 0, 5, 0, 8, 9, 0]
zeros = []
non_zero = []
for i in range(len(a)):
    if a[i]!=0:
        non_zero.append(a[i])
    else:
        zeros.append(a[i])
        
result = non_zero + zeros
print(result)
    
