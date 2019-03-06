





#O(N^2)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        sum1 = 0
        for i in range(len(nums)):
            sum1 = sum1 + nums[i]
        if sum1 < s:
            return 0
        
        #prefix
        pre = []
        for i in range(0,len(nums)):
            if i == 0:
                pre = pre + [nums[0]]
            else:
                pre += [pre[i-1] + nums[i]]
        
        min_val = len(nums)
        for start in range(0,len(nums)):
            for end in range(start,len(nums)):
                cur_val = 0
                if pre[end] - pre[start] + nums[start] >= s:
                    cur_val = end - start + 1
                    if cur_val < min_val:
                        min_val = cur_val   
                
        return min_val






# O(N^3)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        sum1 = 0
        for i in range(len(nums)):
            sum1 = sum1 + nums[i]
        if sum1 < s:
            return 0

        cur_val = 0
        min_val = len(nums)
        for start in range(0, len(nums)):
            for end in range(start, len(nums)):
                interval = 0
                for i in range(start,end+1):
                    interval += nums[i]
                if interval >= s:
                    cur_val = end - start + 1
                    if cur_val < min_val:
                        min_val = cur_val
        return min_val
            
            
       

                
            
            
            
