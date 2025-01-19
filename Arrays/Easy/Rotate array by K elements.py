def left_sort(a,k):  #LEFT
    n = len(a)
    c=k%n

    return a[c:] + a[:c]

def right_sort(a,k):  #RIGHT
    n=len(a)
    c=k%n
    return a[-c:] + a[:-c]

def main(a,k):
    print('left_sort:',left_sort(a,k))
    print('right_sort:',right_sort(a,k))    
    
    
if __name__ == '__main__':
    a=[1,2,3,4,5,6]   
    k=2
    main(a,k)






