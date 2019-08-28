"""
27. Remove element
two pointers to record start and end
"""

### slow point that skip elements
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i in range(len(nums)):
            # nums[i] cover nums[slow]
            nums[slow] = nums[i]
            if nums[i] == val:
                continue
            else:
                slow += 1
        return len(nums[:slow])


### two points to record start and end
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start,end = 0,len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
        return len(nums[:start])


