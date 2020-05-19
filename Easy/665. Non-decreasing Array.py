# 665. Non-decreasing Array
# array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        p = None
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i
        return (not p) or p == n-2 or nums[p-1] <= nums[p+1] or \
               nums[p] <= nums[p+2]