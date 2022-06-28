# https://leetcode.com/problems/valid-anagram/submissions/

from collections import Counter

class Solution:
    def isAnagramNoImports(self, s: str, t: str) -> bool:
        # no imports
        if len(s) != len(t):
            return False
        counterS, counterT = {}, {}
        for charS, charT in zip(s, t):
            counterS[charS] = counterS.get(charS, 0) + 1
            counterT[charT] = counterT.get(charT, 0) + 1
        return counterS == counterT
    
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
