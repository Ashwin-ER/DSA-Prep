
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  #unsorted
        j = i - 1     #sorted
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

if __name__ == '__main__':
    arr = [11,9,29,7,2,15,28]
    insertion_sort(arr)
    print(arr)

    