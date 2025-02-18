def palindeome(n):
    rev = 0
    while n>0:
        ld = n % 10

        rev = (rev*10) + ld

        n = n //10
    return rev


if __name__ == "__main__":
    n = 12315
    print(palindeome(n))
