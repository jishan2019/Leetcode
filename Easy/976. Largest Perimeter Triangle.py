# 976. Largest Perimeter Triangle
# math

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        res = sorted(A, reverse=True)
        for i in range(len(res)-2):
            if sum(res[i+1:i+3]) > res[i]:
                return sum(res[i:i+3])
        return 0