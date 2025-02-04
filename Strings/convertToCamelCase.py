def convertToCamelCase(s):
    res = []
    words = s.split()
    
    res = [words[0].lower()]
    
    for word in words[1:]:
        res.append(word[0].upper() + word[1:].lower())
    
    return "".join(res)



if __name__ == "__main__":
    s = "i got intern at geeksforgeeks"
    print(convertToCamelCase(s))
