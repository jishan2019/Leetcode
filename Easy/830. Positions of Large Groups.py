# 830. Positions of Large Groups
# array


# two pointers
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i = 0 # start of each group
        ans = []
        for j in range(len(S)):
            if j == len(S)-1 or S[j] != S[j+1]:
                if j - i >= 2:
                    ans.append([i, j])
                i = j + 1
        return ans