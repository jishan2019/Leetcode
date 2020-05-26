# 559. Maximum Depth of N-ary Tree
# tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # using BFS to solve
        c,level = root and [root], 0
        while c:
            c, level = [child for node in c for child in node.children], level + 1
        return level