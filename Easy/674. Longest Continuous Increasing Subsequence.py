# 674. Longest Continuous Increasing Subsequence
# array

def findLengthOfLCIS(self, nums: 'List[int]') -> 'int':
    ans = anchor = 0
    for i in range(len(nums)):
        if i and nums[i] <= nums[i-1]:
            anchor = i
        else:
            ans = max(ans, i-anchor+1)
    return ans