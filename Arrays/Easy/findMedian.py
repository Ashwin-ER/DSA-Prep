def findMedian(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]

if __name__ == "__main__":
    arr = [1, 3, 4, 2, 7, 5, 8, 6]
    median = findMedian(arr)
    print(median)
