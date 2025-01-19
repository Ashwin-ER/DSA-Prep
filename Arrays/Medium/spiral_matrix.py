def spiral(arr):
    ans = []
    
    n = len(arr)
    m = len(arr[0])
    
    left = 0
    right = m-1
    top = 0
    bottom = n-1
    
    while (top <= bottom and left <= right):
        for i in range(left, right+1):
            ans.append(arr[top][i])
        top = top + 1
            
        for i in range(top, bottom+1):
            ans.append(arr[i][right])
        right= right -1
        
        if (bottom >= top):
            for i in range(right, left-1, -1):
                ans.append(arr[bottom][i])
            bottom = bottom - 1
                
        if (right>=left):
            for i in range(bottom, top-1, -1):
                ans.append(arr[i][left])
            left = left +1

    return ans


arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
a = spiral(arr)
print(a)
    
    
