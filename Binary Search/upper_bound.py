#MY BRUTE APPROACH 
def upper_bound(a, target):
    n = len(a)
    for i in range(n):
        if a[i] >= target:
            return i  
    return n  

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 8
    upper = upper_bound(a, target)
    print(f"Upper bound of {target} is at index: {upper}")
    
   
# OPTIMAL ONE 
def upper_bound(a, target):
    n = len(a)
    low = 0
    high = n-1
        
    while low <= high:
        mid = (low + high)//2

        if a[mid]>target:
            high = mid -1
        else:
            low = mid +1  
                  
            
        
    
    return low

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 8
    upper = upper_bound(a, target)
    print(f"Upper bound of {target} is at index: {upper}")
