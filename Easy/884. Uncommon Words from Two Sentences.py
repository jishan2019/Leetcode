# 884. Uncommon Words from Two Sentences
# hash table

# using count method is the easiest way
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        count = Counter((A+' '+B).split())
        return [word for word,c in count.items() if c==1]