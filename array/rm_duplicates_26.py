class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        cnt = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt