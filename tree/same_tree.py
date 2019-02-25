# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
            if p == None and q == None:
                # empty tree
                return True
            if p == None:
                return False
            if q == None:
                return False
            
            if p.val != q.val:
                return False
            
            # recursion func
            if self.isSameTree(p.left, q.left) == False:
                return False
            if self.isSameTree(p.right, q.right) == False:
                return False
            
            return True