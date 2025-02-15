def findDuplicates():
    res = []
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                res.append(arr[i])

    return  res

if __name__ == "__main__":
    arr = [1, 3, 4, 2, 1, 7, 7, 5, 8, 6, 6]
    n = len(arr)
    print(findDuplicates())
