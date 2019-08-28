"""
80. Remove Duplicates from Sorted Array II
compare the position of i and slow-1,slow-2
rather than i and i-1, i-2
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # duplicated element no more than twice
        # sorted array
        # avoid out of range
        if len(nums) == 1 or len(nums) == 2: return len(nums)
        slow = 2
        for i in range(2,len(nums)):
            if nums[i] == nums[slow-1] == nums[slow-2]:
                continue
            else:
                nums[slow] = nums[i]
                slow += 1
        return len(nums[:slow])