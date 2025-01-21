def rotations(a, b):
    if len(a)!=len(b):
        return False
    temp = a+b
    if b in temp:
        return True 
    else:
        return False

if __name__ == "__main__":
    a = 'hello'
    b = 'ohell'
    #print(rotations(a, b))
    if rotations(a, b):
        print(f"'{a}' and '{b}' are rotations of each other.")
    else:
        print(f"'{a}' and '{b}' are NOT rotations of each other.")
