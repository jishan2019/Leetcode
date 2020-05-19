# 617. Merge Two Binary Trees
# binary search tree

# using stack to solve this problem
# First create a root node--t, then we have to consider each child node is none or not.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# using recursive to solve
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		if t1 and t2:
			newT = TreeNode(t1.val + t2.val)
			newT.left = self.mergeTrees(t1.left, t2.left)
			newT.right = self.mergeTrees(t1.right, t2.right)
			return newT
		else:
			return t1 or t2
