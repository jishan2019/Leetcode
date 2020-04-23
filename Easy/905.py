# 905. Sort Array By Parity
#
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.


#using two pointers
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A)-1
        while l < r:
            while l<r and A[l]&1==0:
                l += 1
            while l<r and A[r]&1==1:
                r -= 1
            A[l], A[r] = A[r], A[l]
        return A


# second way
class Solution:
    def sortArrayByParity(self, A):
        even = [num for num in A if num & 1 == 0]
        odd = [num for num in A if num & 1 == 1]
        return even + odd