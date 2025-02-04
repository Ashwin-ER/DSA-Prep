def countSubStr(s):
    res = 0
    for i in range(len(s)):
        if s[i] == '1':
            for j in range(i+1, len(s)):
                if s[j] == '1':
                    res = res + 1 
    return res                



if __name__ == "__main__":
    s = "00100101"
    list(s)
    print(countSubStr(s))
