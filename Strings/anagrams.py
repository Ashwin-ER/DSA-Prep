def anagrams(s1,s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    
    if s1 == s2:
        print("this is anagram")
    else:
        print("this is not anagram")
    
if __name__ == "__main__":
    s1 = 'geeks'  
    s2 = 'kseeg'
    anagrams(s1,s2)
