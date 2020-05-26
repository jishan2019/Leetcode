# 94. Binary Tree Inorder Traversal
# hash table; stack; tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #using stack to solve
        stack, ans = [],[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            ans.append(root.val)
            root=root.right
        return ans