import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left = []
    right = []
    mid = []
    
    pivot = random.choice(arr)
    
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            mid.append(i)
    
    return quick_sort(left) + mid + quick_sort(right)

arr = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 78, 7, 2, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)
