# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        {sorted version: [all common]}
        returns values
        """
        anagrams = {}
        for s in strs:
            anagrams.setdefault(tuple(sorted(s)), []).append(s)
        
        return list(anagrams.values())
