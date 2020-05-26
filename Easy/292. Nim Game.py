# 292. Nim Game
# Brainteaser; Minimax

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0