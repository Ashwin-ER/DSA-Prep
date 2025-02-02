def a(arr):
  b = []
  for i in range(0,n):
    if arr[i]!=0:
      b.append(arr[i])
  c = len(arr) - len(b)
  d = b + [0]*c
  return d
  


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    n = len(arr)
    print(a(arr))
