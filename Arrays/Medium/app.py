def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1  

    while mid < high:
        if arr[mid] == 0:
            arr[mid], arr[low]= arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr



arr = [2, 1, 0, 2, 1, 1, 0]
sorted_arr = sort_012(arr)
print("Sorted array:", sorted_arr)