# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne1(self, digits: List[int]) -> List[int]:
        n = len(digits)-1

        while n > -1:
            digits[n] += 1

            if digits[n] == 10:
                digits[n] = 0
            else:
                return digits

            n -= 1
            
        digits.insert(0, 1)
        
        return digits
    
    # sort of cheating 1 liner
    def plusOneOneLine(self, digits: List[int]) -> List[int]:
        return list(str(int("".join([str(n) for n in digits])) + 1))
