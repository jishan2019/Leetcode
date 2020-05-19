# 661. Image Smoother
# array

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        import itertools
        R, C = len(M), len(M[0])
        res = [[0]*C for _ in range(R)]
        offset = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
        for i in range(R):
            for j in range(C):
                points = [M[i+x][j+y] for x, y in offset
                          if 0<=i+x<R and 0<=j+y<C]
                res[i][j] = sum(points) // len(points)
        return res