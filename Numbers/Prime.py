def checkPrime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i==0:
            cnt = cnt + 1
    if cnt == 2:
        return 'True'
    else:
        return 'False'

if __name__ == "__main__":
    n = 3
    print(checkPrime(8))
    print(checkPrime(n))
    '''isPrime = checkPrime(n)
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

'''
