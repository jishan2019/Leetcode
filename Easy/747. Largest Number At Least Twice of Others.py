# 747. Largest Number At Least Twice of Others
# array


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_v = max(nums)
        if all(max_v >= 2*x for x in nums if x!=max_v):
            return nums.index(max_v)
        return -1