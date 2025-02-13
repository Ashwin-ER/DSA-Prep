def printOrder():
    print(sorted(set(arr)))

    for i in range(n//2):
        print(arr[i],end=',')


    for j in range(n-1, n//2, -1):
        print(arr[j], end=',')



if __name__ == "__main__":
    arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
    n = len(arr)
    printOrder()
