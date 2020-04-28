# 5. Longest Palindromic Substring
#NP; BFS
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

## reference: https://segmentfault.com/a/1190000003914228 (Manacher Algorithm)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]



#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if i-maxLen>=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i-maxLen>=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                # print(s[i-maxLen:i+1], s[i-maxLen:i+1][::-1])
                start = i - maxLen
                maxLen += 1
        return s[start:start+maxLen]

