# 485. Max Consecutive Ones
# Array

# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

#1
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        from itertools import groupby
        count = 0
        for num, res in groupby(nums):
            if num == 1:
                count = max(count, len(list(res)))
        return count