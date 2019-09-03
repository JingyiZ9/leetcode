# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s: return 0
        # min subarray sum >= s
        # O(n) complexity
        sumVal = left = 0
        minLen = len(nums) +1
        for i in range(len(nums)):
            sumVal += nums[i]
            if sumVal >= s:
                # sumVal >= s
                # shrink the left pos
                while sumVal - nums[left] >= s:
                    sumVal -= nums[left]
                    left += 1
                if minLen > i-left+1:
                    minLen = i-left+1
                    
        if minLen > len(nums):
            return 0
        else:
            return minLen
                
# 567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return true if s1 is the substr of s2
        if len(s2) < len(s1): return False
        n = len(s1)
        left, right = 0, n-1
        c = collections.Counter(s1)
        s = collections.Counter(s2[left:right])
        while right < len(s2):
            # increase right
            s[s2[right]] += 1
            if s == c:
                return True
            # decrease left
            s[s2[left]] -= 1
            # if zero, remove
            if s[s2[left]] == 0:
                del s[s2[left]]
            left += 1
            right +=1
        return False

# 438. Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return
        n = len(p)
        left, right = 0, n-1
        res = []
        dict_p = collections.Counter(p)
        dict_s = collections.Counter(s[left:right])
        while right < len(s):
            dict_s[s[right]] += 1
            if dict_s == dict_p:
                res += [left]
            dict_s[s[left]] -= 1
            if dict_s[s[left]] == 0:
                del dict_s[s[left]]
            left += 1
            right += 1
        return res


