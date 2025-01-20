def palindrome():
    b = a[::-1]
    if a==b:
        print(f'{a} is palindrome') 
    else:
        print(f'{a} is not a palindrome')
    

if __name__ == "__main__":
    a = 'madam'
    palindrome()
