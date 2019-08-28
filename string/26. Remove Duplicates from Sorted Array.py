"""
26. Remove Duplicates from Sorted Array
easy
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[slow] = nums[i]
                slow += 1
        return len(nums[:slow])