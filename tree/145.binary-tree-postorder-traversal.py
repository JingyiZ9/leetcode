#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (46.73%)
# Total Accepted:    240K
# Total Submissions: 509.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        # root -> right -> left, then inverse
        res, stack = [], []
        while stack or root:
            if root:
                stack += [root]
                res += [root.val]
                root = root.right
            else:
                cur_root = stack.pop()
                root = cur_root.left
                
        return res[::-1]

########################
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

