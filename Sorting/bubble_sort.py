def bubble_sort():
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 78,7 ,2, 2, 1]
print(bubble_sort())
