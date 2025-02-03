def maxProfit(arr):
    maxPro = 0
    minPrice = arr[0]
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro

arr = [7, 1, 5, 3, 6, 4]
maxPro = maxProfit(arr)
print("Max profit is:", maxPro)



#Next
def maxProfit(arr,n):
  small = arr[0]
  maxi = 0
  for i in range(1,n):
    small = min(small, arr[i])
    maxi = max(maxi, arr[i]-small)
    
  
  return maxi

  
if __name__ == "__main__":
    arr =  [7, 10, 1, 3, 6, 9, 2]
    n = len(arr)
    print(maxProfit(arr, len(arr)))
   
