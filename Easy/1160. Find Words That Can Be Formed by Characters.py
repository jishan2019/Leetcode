# 1160. Find Words That Can Be Formed by Characters
# hash table; array

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        num = collections.Counter(chars)
        return sum(len(w) for w in words if not collections.Counter(w)-num)