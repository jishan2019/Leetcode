"""485. Max Consecutive Ones Easy

Companies: Amazon

link: https://leetcode.com/problems/max-consecutive-ones/

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""

"""Solution:

# method 1
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Find the maximum till now.
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 1
         return max(max_count, count)        
# method 2                
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        from itertools import groupby
        count = 0
        for d, group in groupby(nums):
            if d == 1:
                count = max(count, len(list(group)))
        return count
"""


from itertools import groupby
def findMaxConsecutiveOnes(nums):
	count = 0
	for d, group in groupby(nums):
		if d == 1:
			count = max(count, len(list(group)))
	return print(count)

findMaxConsecutiveOnes(nums = [1,1,0,1,1,1])
