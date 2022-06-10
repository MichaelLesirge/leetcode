# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]
    
    def isPalindromeOneLine(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
