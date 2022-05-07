# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        """
        add each open bracket to stack
        if its closed check the last open brack to see if it is a match 
        
        empty lists are false, aka (stack != []) or (len(stack) > 0)
        """
        
        stack = []
        
        matcher = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in matcher:
                if not ((stack) and (stack.pop() == matcher[char])):
                    return False
            else:
                stack.append(char)
        
        return not stack
