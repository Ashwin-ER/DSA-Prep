def reverse_array(arr,n):
  a = arr[0:k]
  b = a[::-1]
  c = arr[k:]
  print(b+c)
  
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    k = 3
    reverse_array(arr,n)
