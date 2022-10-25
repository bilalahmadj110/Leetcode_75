# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        
        tree = []
        queue = deque([root])
        while queue:
            level = []
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                
                level.append(node.val)
                
            queue = deque(temp)
            tree.append(level)
            
        return tree
            