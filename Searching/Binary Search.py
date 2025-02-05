
def binary_search(a, target):
    n = len(a)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        if a[mid] == target:
            return mid
        elif target>a[mid]:
            low = mid + 1
        else:
            high = mid - 1
             
    return -1

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    print(binary_search(a, target))
    
