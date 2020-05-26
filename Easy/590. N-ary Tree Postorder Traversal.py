# 590. N-ary Tree Postorder Traversal
# tree

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        return sum([self.postorder(child) for child in root.children], []) + [root.val]