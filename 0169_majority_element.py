# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        chance = 0
        
        for num in nums:
            chance += [-1, 1][num == current]
            
            if chance < 0:
                current = num
                chance = 1
        
        return current
