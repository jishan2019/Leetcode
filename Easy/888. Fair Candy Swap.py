# 888. Fair Candy Swap
# array

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A)) // 2
        set_b = set(B)
        for a in A:
            if diff + a in set_b:
                return a, diff + a