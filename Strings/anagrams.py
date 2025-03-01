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


#leetcode 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        else:
            return False


solution = Solution()
s = "anagram"
t = "nagaram"
result = solution.isAnagram(s, t)
print(result) 
