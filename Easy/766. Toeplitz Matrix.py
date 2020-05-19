# 766. Toeplitz Matrix
#  array

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(x==0 or y==0 or matrix[x-1][y-1]==val
               for x, rows in enumerate(matrix)
               for y, val in enumerate(rows))