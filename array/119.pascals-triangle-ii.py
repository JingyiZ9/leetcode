#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (41.90%)
# Total Accepted:    183.8K
# Total Submissions: 438.5K
# Testcase Example:  '3'
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        result = []
        list_val = [1,1]
        
        for i in range(3,rowIndex+2):
            list_next = [0] * i
            list_next[0] = 1
            list_next[-1] = 1
            for j in range(1,len(list_val)):
                list_next[j] = list_val[j-1] + list_val[j]
         
            result.append(list_next)
            list_val = list_next
    
        return result[rowIndex-2]
        
