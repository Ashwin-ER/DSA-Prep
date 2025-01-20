def duplicate(a):
    dup = set()
    seen = set()
    for char in a:
        if char in seen:
            dup.add(char)
        else:
            seen.add(char)
    print(dup)
    

if __name__ == "__main__":
    a = 'AshwinAshwin'
    duplicate(a)
