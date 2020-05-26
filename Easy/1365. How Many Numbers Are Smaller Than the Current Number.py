# 1365. How Many Numbers Are Smaller Than the Current Number
# array; hashtable

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        for i, d in enumerate(sorted(nums)):
            indices.setdefault(d, i)
        return [indices[d] for d in nums]

