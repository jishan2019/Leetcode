# 1128. Number of Equivalent Domino Pairs
# array

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = collections.Counter(tuple(sorted(d)) for d in dominoes)
        return sum(v*(v-1)//2 for v in dominoes.values())