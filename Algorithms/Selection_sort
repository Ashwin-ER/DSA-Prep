def selection_sort(arr):
    #min = i
    size = len(elements)
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if arr[min] > arr[j]:
                min = j
        if i != min: 
            arr[min] , arr[i] = arr[i] , arr[min]
    return arr


if __name__ == '__main__':
    elements = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 78,7 ,2, 2, 1]
    print(selection_sort(elements))
