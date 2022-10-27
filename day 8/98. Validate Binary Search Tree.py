# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import sys

class Solution:
    
    def isValidBST(self, root) -> bool:
        return self.isValid(root,  -(sys.maxsize * 2 + 1), sys.maxsize * 2 + 1)

    def isValid(self, root, mn, mx):
        if root is None:
            return True
        if root.val >= mx or root.val <= mn:
            return False
        return self.isValid(root.left, mn, root.val) and self.isValid(root.right, root.val, mx)
        
        



