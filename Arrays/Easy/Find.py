def find(arr, num):
    if num in arr:
        print("Present")
    else:
        print("Not Present")

arr = [1, 3, 7, 9, 45]
num = int(input("Enter num: "))
find(arr, num)
