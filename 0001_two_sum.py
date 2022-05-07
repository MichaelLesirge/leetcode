# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        
        for index, num in enumerate(nums):
            if num in remainders:
                return [index, remainders[num]]
            remainders[target-num] = index
