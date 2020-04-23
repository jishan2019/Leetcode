# 922. Sort Array By Parity II
##array sort

# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#
# You may return any answer array that satisfies this condition.

#two pointers
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] & 1 == 1:
                while A[j] & 1 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

#slicing
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [None] * len(A)
        res[::2] = (num for num in A if num & 1 == 0)
        res[1::2] = (num for num in A if num & 1 == 1)
        return res