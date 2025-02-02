#arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

def sortInWave(arr,n):
  arr.sort()
  for i in range(0,n-1,2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
  
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sortInWave(arr, len(arr))
    for i in range(0,len(arr)):
      print (arr[i],end=" ")
