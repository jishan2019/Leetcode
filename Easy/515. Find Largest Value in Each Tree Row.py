# 515. Find Largest Value in Each Tree Row
# tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ans, levels = [], root and [root]
        while levels:
            ans.append(max(x.val for x in levels))
            levels = [k for n in levels for k in (n.left, n.right) if k]
        return ans