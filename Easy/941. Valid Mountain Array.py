# 941. Valid Mountain Array
# array

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # two pointers to solve
        l, r, n = 0, len(A)-1, len(A)
        while l < r and A[l] < A[l+1]: l += 1
        while r > 0 and A[r] < A[r-1]: r -= 1
        return 0 < l==r < n-1