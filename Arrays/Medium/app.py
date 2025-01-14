


def leader_array(arr, n):
    ans = []
  
    for i in range(n):
        leader = True

        for j in range(i+1, n):
            if arr[j] > arr[i]:
                leader = False
                break

        if leader:
            ans.append(arr[i])

    return ans

if __name__ == '__main__':
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    print(leader_array(arr, n))

    


