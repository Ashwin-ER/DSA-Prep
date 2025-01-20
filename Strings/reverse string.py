def rev():
    return a[::-1]

if __name__ == "__main__":
    a = "GeeksforGeeks"
    print(rev())
    
    
#ANOTHER APPROACH
def rev(a):
    ans = []
    for i in range(len(a)-1, -1 ,-1):
        ans.append(a[i])
    return "".join(ans)     

if __name__ == "__main__":
    a = "GeeksforGeeks"
    print(rev(a))
