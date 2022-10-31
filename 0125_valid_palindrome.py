# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [a.lower() for a in s if a.isalnum()]
        return all(a==b for a, b in zip(s, reversed(s)))
