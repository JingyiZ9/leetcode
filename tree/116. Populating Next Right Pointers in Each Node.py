#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
bfs: take advantage of queue
note: we need to record the len of queue
        and set i < n-1 node.next = queue[0]
        so that i = n-1 node.next = None
        Initially, all next pointers are set to NULL
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        # bfs
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i < n-1:
                    node.next = queue[0]
                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]
        return root

"""
recursion:
    perfect binary tree (完全二叉树) must has both left and right node
    so root.left.next = root.right
    as for right node, if root.next != None, then root.right.next = root.next.left
    else None
"""
    class Solution:
        def connect(self, root: 'Node') -> 'Node':
            if not root: return None
            if root.left:
                root.left.next = root.right
            if root.right:
                if root.next:
                    root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
            return root