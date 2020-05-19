# 985. Sum of Even Numbers After Queries
# array

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum_even = sum(x for x in A if x & 1 == 0)
        for v, i in queries:
            if A[i] & 1 == 0:
                sum_even -= A[i]
            A[i] += v
            if A[i] & 1 == 0:
                sum_even += A[i]
            res.append(sum_even)
        return res