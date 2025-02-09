def selection_sort():
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 78,7 ,2, 2, 1]
print(selection_sort())
