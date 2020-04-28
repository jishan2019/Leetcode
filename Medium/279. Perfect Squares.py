# 279. Perfect Squares
#NP; BFS

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

## We need to find the minimum n : f(n) = min ( f(n-1^2),f(n-1^2),...,f(0)) +1

class Solution:
    dp_0 = [0]
    def numSquares(self, n: int) -> int:
        dp = self.dp_0
        while len(dp) <= n:
            # dp.append(min(dp[len(dp)-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1)
            dp.append(min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1)
        return dp[n]