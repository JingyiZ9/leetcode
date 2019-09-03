# 242. Valid Anagram

# 76. Minimum Window Substring 最小窗口子串 [hard]
"""
滑动窗口 sliding window
右边界无法扩大了后才开始收缩左边界
先遍历一遍t，再遍历s，遇到xiangxiang如果d中数值等于0，表明当前res包含了t，如果d中数值
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for i in range(len(t)):
            if t[i] not in d:
                d[t[i]] = 1
            else:
                d[t[i]] += 1
        
        start = minstart = cnt = 0
        min_val = len(s) +1
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] -= 1
                if d[s[i]] >= 0:
                    cnt += 1
            while cnt == len(t):
                if min_val > i-start+1:
                    min_val = i-start+1 
                    minstart = start
                # shrink the start to minstart
                if s[start] in d:
                    d[s[start]] += 1
                    if d[s[start]] > 0:
                        cnt -= 1
                start += 1
        if min_val > len(s):
            return ""
        else:
            return s[minstart:minstart+min_val]

# 205. Isomorphic Strings 同构字符串

# 3. Longest Substring Without Repeating Characters 最长无重复子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val = leftPos = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and leftPos <= d[s[i]]:
                # repeat s[i] in str, update the left position
                leftPos = d[s[i]] +1
            else:
                max_val = max(max_val, i-leftPos+1)
            d[s[i]] = i
        return max_val
                