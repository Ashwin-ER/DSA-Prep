def intersection(arr1, arr2):  #1
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                result.append(arr1[i])
                break 
    return result

def inter(arr1, arr2):   #2
    set1=set(arr1)
    set2=set(arr2)
    #a=set1 and set2
    return list(set1 & set2)

arr1 = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 1, 12]
print(intersection(arr1, arr2))
print(inter(arr1, arr2))


