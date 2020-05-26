# 628. Maximum Product of Three Numbers
# array, math

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ary = sorted(nums)
        return max((ary[0]*ary[1]*ary[-1], ary[-3]*ary[-2]*ary[-1]))


# try to use heapq to solve