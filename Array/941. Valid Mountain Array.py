# 941. Valid Mountain Array
# array


# solution 1
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # two pointers to solve
        l, r, n = 0, len(A)-1, len(A)
        while l < r and A[l] < A[l+1]: l += 1
        while r > 0 and A[r] < A[r-1]: r -= 1
        return 0 < l==r < n-1


# solution 2
# one pass
# Complexity Analysis
# Time Complexity: O(N)O(N), where NN is the length of A.
# Space Complexity: O(1)O(1).
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1


# method 2
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # two pointers to solve
        l, r, n = 0, len(A)-1, len(A)
        while l < r and A[l] < A[l+1]: l += 1
        while r > 0 and A[r] < A[r-1]: r -= 1
        return 0 < l==r < n-1