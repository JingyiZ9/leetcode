# 判断序列二叉树
#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        verify a binary tree
        two none nodes correspond to a legal root node
        number,#,# return to a # node
        use a stack to store
        """
        stack = []
        for node in preorder.split(','):
            # split the list preorder by ',' and enter into stack
            stack += [node]
            while len(stack)>=3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop(), stack.pop(), stack.pop()
                stack += ['#']
        return len(stack) == 1 and stack.pop() == '#'

