# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while end >= start:
            mid = (start+end) // 2
            mid_num = nums[mid]
            if mid_num > target:
                end = mid-1
            elif mid_num < target:
                start = mid+1
            else:
                return mid
        return -1
