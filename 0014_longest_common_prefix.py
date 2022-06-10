# https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for chars in zip(*strs):
            if all((chars[0]==char) for char in chars):
                pre += chars[0]
            else:
                break
        return pre
