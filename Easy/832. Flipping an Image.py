# 832. Flipping an Image
# array

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[x ^ 1 for x in reversed(row)] for row in A]