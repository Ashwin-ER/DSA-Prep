#MY BRUTE APPROACH 
def (a, target):
    n = len(a)
    for i in range(n):
        if a[i] >= target: 
            return i  
    return n  

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 8
    lower = lower_bound(a, target)
    print(f"lower bound of {target} is at index: {lower}")
    
#BRUTE: NOT MY APPROACH
def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(n):
        if arr[i] >= x:
            #lower bound found
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)



    
# OPTIMAL ONE 
def lower_bound(a, target):
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
    lower = lower_bound(a, target)
    print(f"lower bound of {target} is at index: {lower}")
