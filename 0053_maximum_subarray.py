# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        heard of this one
        """
        current = 0
        current_max = nums[0]
        
        for num in nums:
            current = max(current+num, num)
            
            # current_max = max(current, current_max)
            if current > current_max:
                current_max = current
            
        return current_max
