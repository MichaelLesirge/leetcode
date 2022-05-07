# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        some version of binary seach
        if it is not found return as close as possible probbly left
        """
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]
            if mid_num > target:
                right = mid-1
            elif mid_num < target:
                left = mid+1
            else:
                return mid
        
        return left
