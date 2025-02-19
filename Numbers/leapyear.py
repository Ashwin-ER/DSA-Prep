
def leapyear(n):
    if n%4==0 and n%100!=0:
        print("leap")
    else:
        print('not a leap')


if __name__ == "__main__":
    n = 12315
    print(leapyear(n))
