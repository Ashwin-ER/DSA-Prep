def find_missing_number(arr,n):
    miss_num = []
    sort = set(arr)
    for i in range(1,n+1):
        if i not in sort:
            miss_num.append(i)
    return miss_num

arr = [1, 2, 4, 6, 7, 9]  
n = 9
print("Missing number:", find_missing_number(arr,n))
