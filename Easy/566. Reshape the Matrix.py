# 566. Reshape the Matrix
# array

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        a = [x for row in nums for x in row]
        n = len(a)
        if r*c != n:
            return nums
        return [a[i*c:i*c+c] for i in range(r)]