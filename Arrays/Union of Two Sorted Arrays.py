#METHOD 1
a = [0, 1, 2, 0, 5, 0, 8, 9, 0]
b = [1, 2, 3, 4, 5]

print(sorted(set(a+b)))

#METHOD 2
def union(arr1, arr2):
    s = set()
    union = []
    
    for num in arr1:
        s.add(num)
    
    for num in arr2:
        s.add(num)
    
    for num in s:
        union.append(num)
    
    return union

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(union)




