#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (44.40%)
# Total Accepted:    226.5K
# Total Submissions: 510K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        result = []
        list_val = [1]
        result.append(list_val)
        list_val = [1,1]
        result.append(list_val)
        
        for i in range(3,numRows+1):
            list_next = [0] * i
            list_next[0] = 1
            list_next[-1] = 1
            
            for j in range(1,len(list_val)):
                list_next[j] = list_val[j-1] + list_val[j]
                
            result.append(list_next)
            list_val = list_next
        
        return result
            
        
