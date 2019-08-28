"""
28. Implement strStr()
判断haystack数组中是否包含needle
"""

### brutal solution: O(n^2) time
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if j == len(needle): return i
                if i+j == len(haystack): return -1
                if haystack[i] != needle[j]: break

######
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1