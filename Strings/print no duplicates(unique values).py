def duplicate(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return ' '.join(b)  #m a d
    return b            #['m', 'a', 'd']

if __name__ == "__main__":
    a = 'madam'
    print(duplicate(a))
