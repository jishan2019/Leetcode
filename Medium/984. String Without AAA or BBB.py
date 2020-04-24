# 984. String Without AAA or BBB

#greedy algorithm

# Given two integers A and B, return any string S such that:
#
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.


# Example 1:
#
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.

# Example 2:
#
# Input: A = 4, B = 1
# Output: "aabaa"



#1
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = ''
        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans += 'a'
            else:
                B -= 1
                ans += 'b'
        return ans



#2
# if A=B  ==> the pattern can be: abab, baba, ...
# if A>B  ==> the pattern can be: aab, aabab,... (first write out aa, then write out b, an so on)
# if A<b  ==> the pattern can be: bba, bbaba,...

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A > B:
            k = min(A - B, B)
            return 'aab' * k + 'ab' * (B - k) + 'a' * (A - k - B)
        else:
            k = min(B - A, A)
            return 'bba' * k + 'ba' * (A - k) + 'b' * (B - k - A)