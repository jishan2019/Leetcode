# 1010. Pairs of Songs With Total Durations Divisible by 60
# hash table

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        c=collections.defaultdict(int)
        for t in time:
            ans += c[-t%60]
            c[t%60] += 1
        return ans