def RearrangebySign(A, n):
    pos = []
    neg = []
    
    for i in range(n):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
    
    if len(pos) < len(neg):
        for i in range(len(pos)):
            A[2*i] = pos[i]
            A[2*i+1] = neg[i]
        
        index = len(pos)*2
        for i in range(len(neg)-len(pos)):
            A[index] = neg[len(pos)+i]
            index += 1
    
    else:
        for i in range(len(neg)):
            A[2*i] = pos[i]
            A[2*i+1] = neg[i]
        
        index = len(neg)*2
        for i in range(len(pos)-len(neg)):
            A[index] = pos[len(neg)+i]
            index += 1
    
    return A

n = 6
A = [1, 2, -4, -5, 3, 4]

ans = RearrangebySign(A, n)
print(ans)

