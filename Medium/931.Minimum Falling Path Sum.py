# 931. Minimum Falling Path Sum
#NP


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        for i in range(R-2, -1, -1):
            for j in range(C):
                path = slice(max(0, j-1), min(C, j+2))
                A[i][j] += min(A[i+1][path])
        return min(A[0])



#2 solution from leetcode
class Solution(object):
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()
            for i in xrange(len(row)):
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])


