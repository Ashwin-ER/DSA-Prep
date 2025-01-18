def rotate(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in range(n):
        arr[i].reverse()
        
    return 




if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(arr)
    print("Rotated Image")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
    
