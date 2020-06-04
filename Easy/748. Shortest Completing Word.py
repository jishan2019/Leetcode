# 748. Shortest Completing Word
# hash table

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        ans=''
        licenseplate=''.join(x for x in licensePlate.lower() if x.isalpha())  # isalpha() returns true is all characters in the string are alphabets
        for w in words:
            temp=list(w.lower())
            for l in licenseplate:
                if l in temp:
                    temp.remove(l)
                else:
                    break
            else:
                if len(w) < len(ans) or ans=='':
                    ans=w
        return ans