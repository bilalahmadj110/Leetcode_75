
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque
class Solution:
    
    def preorder(self, root):
        l = []
        d = [root]
        while len(d):
            pop = d.pop(0)
            if pop is None:
                continue
            l.append(pop.val)
            d[0:0] = pop.children

        return l