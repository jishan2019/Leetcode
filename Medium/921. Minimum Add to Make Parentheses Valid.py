# 921. Minimum Add to Make Parentheses Valid
# stack; greedy; string

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans1 = ans2 = 0
        for sign in S:
            ans2 += 1 if sign=='(' else -1
            if ans2 == -1:
                ans1 +=1
                ans2 +=1
        return ans1+ans2