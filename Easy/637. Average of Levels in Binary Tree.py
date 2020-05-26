# 637. Average of Levels in Binary Tree
# tress

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans, level = [], root and [root]
        while level:
            ans.append(sum(n.val for n in level)/len(level))
            level=[k for n in level for k in (n.left,n.right) if k]
        return ans