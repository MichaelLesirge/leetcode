# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        offset = 0
        highest = -101  # float("-inf")
        
        for num in nums:            
            if num > highest:
                highest = num
                nums[offset] = num
                offset+=1
        
        return offset
