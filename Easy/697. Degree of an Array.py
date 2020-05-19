# 697. Degree of an Array
# array

# using dict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = collections.defaultdict(int)
        left, right = {}, {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            c[num] += 1
        res = len(nums)
        degree = max(c.values())
        for num, count in c.items():
            if count == degree:
                res = min(res, right[num]-left[num]+1)
        return res