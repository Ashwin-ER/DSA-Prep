def print_duplicates(s):
    duplicates = set()
    for char in s:
        if s.count(char) > 1:  
            duplicates.add(char)

    print("Duplicate characters in the string:")
    
    print(list(duplicates))

s = "geeksforgeeks"
print_duplicates(s)

