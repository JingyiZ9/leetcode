#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (44.94%)
# Total Accepted:    34K
# Total Submissions: 75.4K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# 
# Note:
# 
# 
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].
# 
# 
# bisect function
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1

        pos = bisect_left(nums, target, lower, upper)
        if nums[pos] == target:
            return pos
        else:
            return -1

#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1
            
        while lower <= upper:
            mid = (upper + lower) // 2
            val = nums[mid]
            if val > target:
                upper = mid - 1
            elif val < target:
                lower = mid + 1
            else:
                return mid
        return -1
        

