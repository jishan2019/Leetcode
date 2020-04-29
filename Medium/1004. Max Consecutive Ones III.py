# 1004. Max Consecutive Ones III
#Array

# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
# Return the length of the longest (contiguous) subarray that contains only 1s.
#
# Example 1:
#
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation:
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
#
# Example 2:
#
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation:
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.



#using sliding window
class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        d = [-1]
        for i in range(len(a)):
            if a[i] == 0:
                d.append(i)
        d.append(len(a))
        if k >= len(d)-2:
            return len(a)
        ans = 0
        for i in range(0,len(d)-k-1):
            ans = max(ans, d[i+k+1]-d[i]-1)
        return ans
