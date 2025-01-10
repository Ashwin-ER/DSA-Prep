#BRUTE 
def two_sum(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n): 
            if arr[i]+arr[j]==target:
                print(i,j)
                #return [i,j]
    return [i,j]
    

arr = [1, 2, 3, 4, 5]
target = 7
two_sum(arr)

#OPTIMAL
def two_sum(arr, target):
    set(sorted(arr))
    left, right = 0, n-1
    while right > left:
        current = arr[left] + arr[right]
        if current == target:
            return 'Yes'
        elif current < target:
            left = left + 1
        else:
            right = right -1
        print(arr[left],arr[right])
    return 'No'
    

if __name__ == "__main__":
    n = 5
    arr = [2, 6, 5, 8, 11]
    target = 14
    ans = two_sum(arr, target)
    print("This is the answer for variant 1:", ans)

