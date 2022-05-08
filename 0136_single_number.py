# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        had to cheat for this one, had no idea how XOR worked
        """
        ans = 0
        for num in nums:
            ans ^= num 
            
        return ans
            
        
