# 942. DI String Match
# math

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l = r = 0
        ans = [0]
        for s in S:
            if s == 'I':
                r += 1
                ans.append(r)
            else:
                l -= 1
                ans.append(l)
        return [x-l for x in ans]