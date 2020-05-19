# 532. K-diff Pairs in an Array
# array

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        c = Counter(nums)
        res = 0
        for num, count in c.items():
            if (k == 0 and count > 1) or (k > 0 and num+k in c):
                res += 1
        return res