# https://leetcode.com/problems/remove-element/solutions/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = len(nums)
        while i < len(nums):
            if nums[i] == val:
                nums[i:] = nums[i+1:]
            else:
                i += 1

    def removeElementWithBuiltins(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

