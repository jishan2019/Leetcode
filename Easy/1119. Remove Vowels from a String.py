"""
1119. Remove Vowels from a String--Easy

Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:
Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"


Example 2:
Input: s = "aeiou"
Output: ""


Constraints:
1 <= s.length <= 1000
s consists of only lowercase English letters.

"""


"""
Solution:
"""
class Solution1:
    def removeVowels(self, S: str) -> str:
        s = set('aeiou')
        ret = ""
        for ch in S:
            if ch not in s:
                ret += ch
        return ret

class Solution2:
    def removeVowels(self, S):
        return "".join(c for c in S if c not in "aeiou")

class Solution3:
    def removeVowels(self, S):str
        return re.sub('a|e|i|o|u', '', S)