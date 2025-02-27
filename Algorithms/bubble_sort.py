def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
        if not swapped: 
            break
    return arr 
    
             
             

if __name__ == '__main__':
    arr = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4, -20]
    arr1 = ["mona", "dhaval", "aamir", "tina", "chang"]
    n = len(arr1)
    print(bubble_sort(arr))
    print(bubble_sort(arr1))
    
