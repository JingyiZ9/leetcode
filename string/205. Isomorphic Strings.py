# 205. Isomorphic Strings
"""
judge s and t are isomorphic strings
s and t are same length
"""
# method 1: one to one function
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s,t) and self.helper(t,s)
    
    def helper(self,str1,str2):
        d = {}
        # str1 and str2 are same length
        for i in range(len(str1)):
            if str1[i] not in d:
                d[str1[i]] = str2[i]
            else:
                if d[str1[i]] != str2[i]:
                    return False
        return True

# method 2: hashtab
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # ascii has 256 space
        # ord() get the unique location
        map1 = [0]*256
        map2 = [0]*256
        for i in range(len(s)):
            if map1[ord(s[i])] != map2[ord(t[i])]:
                return False
            map1[ord(s[i])] = i+1
            map2[ord(t[i])] = i+1
        return True