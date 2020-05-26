# 1170. Compare Strings by Frequency of the Smallest Character
# array; string



class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        quer = [q.count(min(q)) for q in queries]
        word = [w.count(min(w)) for w in words]
        return [sum(q < w for w in word) for q in quer]